"""Ad Account MCP Server using Facebook Business SDK."""

from typing import Any, TypedDict

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.adobjects.savedaudience import SavedAudience
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from ..config import extract_pagination_info, resolve_account_id


class AdAccountResponse(TypedDict):
    success: bool
    data: dict[str, Any] | list[dict[str, Any]]


class PaginatedResponse(TypedDict):
    success: bool
    data: list[dict[str, Any]]
    pagination: dict[str, Any]


class ErrorResponse(TypedDict):
    error: str


# Field constants for better type safety and maintainability
class AdAccountFields:
    """Ad Account field constants using SDK Field enums."""

    BASIC_FIELDS = [
        AdAccount.Field.id,
        AdAccount.Field.account_id,
        AdAccount.Field.name,
        AdAccount.Field.account_status,
        AdAccount.Field.currency,
        AdAccount.Field.timezone_name,
        AdAccount.Field.business,
        AdAccount.Field.amount_spent,
        AdAccount.Field.balance,
        AdAccount.Field.spend_cap,
        AdAccount.Field.created_time,
        AdAccount.Field.owner,
        AdAccount.Field.capabilities,
        AdAccount.Field.min_daily_budget,
    ]


class CustomAudienceFields:
    """Custom Audience field constants using SDK Field enums."""

    BASIC_FIELDS = [
        CustomAudience.Field.id,
        CustomAudience.Field.name,
        CustomAudience.Field.description,
        CustomAudience.Field.approximate_count_lower_bound,
        CustomAudience.Field.approximate_count_upper_bound,
        CustomAudience.Field.subtype,
        CustomAudience.Field.time_created,
        CustomAudience.Field.time_updated,
    ]


class SavedAudienceFields:
    """Saved Audience field constants using SDK Field enums."""

    BASIC_FIELDS = [
        SavedAudience.Field.id,
        SavedAudience.Field.name,
        SavedAudience.Field.targeting,
        SavedAudience.Field.time_created,
        SavedAudience.Field.time_updated,
    ]


ad_account_server = FastMCP(
    name="FacebookAdAccount",
    instructions="Facebook Ad Account management server providing tools for ad account operations.",
)


@ad_account_server.tool
def get_ad_account(account_id: str | None = None) -> AdAccountResponse | ErrorResponse:
    """Get ad account information.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)

    Returns:
        Ad account information with all available fields
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        account = AdAccount(account_id)
        account_data = account.api_get(fields=AdAccountFields.BASIC_FIELDS)

        return {"success": True, "data": dict(account_data)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_account_server.tool
def get_ad_account_users(
    account_id: str | None = None, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get users associated with an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        limit: Maximum number of users to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of users with access to the ad account and pagination info
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        account = AdAccount(account_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        # Note: User fields don't have Field enums in the SDK, using strings as required
        users_cursor = account.get_assigned_users(
            fields=["id", "name", "email", "role", "permissions"], params=params
        )

        users_list = [dict(user) for user in users_cursor]
        pagination_info = extract_pagination_info(users_cursor)

        return {"success": True, "data": users_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_account_server.tool
def get_ad_account_activities(
    account_id: str | None = None, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get recent activities for an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        limit: Maximum number of activities to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of recent account activities and pagination info
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        account = AdAccount(account_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        # Note: Activity fields don't have Field enums in the SDK, using strings as required
        activities_cursor = account.get_activities(
            fields=["event_time", "event_type", "extra_data", "object_id", "object_name"],
            params=params,
        )

        activities_list = [dict(activity) for activity in activities_cursor]
        pagination_info = extract_pagination_info(activities_cursor)

        return {"success": True, "data": activities_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_account_server.tool
def get_ad_account_custom_audiences(
    account_id: str | None = None, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get custom audiences for an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        limit: Maximum number of custom audiences to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of custom audiences and pagination info
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        account = AdAccount(account_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        audiences_cursor = account.get_custom_audiences(
            fields=CustomAudienceFields.BASIC_FIELDS,
            params=params,
        )

        audiences_list = [dict(audience) for audience in audiences_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(audiences_cursor, "_finished_iteration")
            and not audiences_cursor._finished_iteration
        ):
            if hasattr(audiences_cursor, "params") and "after" in audiences_cursor.params:
                pagination_info["next_cursor"] = audiences_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": audiences_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_account_server.tool
def get_ad_account_saved_audiences(
    account_id: str | None = None, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get saved audiences for an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        limit: Maximum number of saved audiences to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of saved audiences and pagination info
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        account = AdAccount(account_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        audiences_cursor = account.get_saved_audiences(
            fields=SavedAudienceFields.BASIC_FIELDS,
            params=params,
        )

        audiences_list = [dict(audience) for audience in audiences_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(audiences_cursor, "_finished_iteration")
            and not audiences_cursor._finished_iteration
        ):
            if hasattr(audiences_cursor, "params") and "after" in audiences_cursor.params:
                pagination_info["next_cursor"] = audiences_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": audiences_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
