"""Ad Set MCP Server using Facebook Business SDK."""

from typing import Any, TypedDict

from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from ..config import extract_pagination_info


class AdSetResponse(TypedDict):
    success: bool
    data: dict[str, Any] | list[dict[str, Any]]


class PaginatedResponse(TypedDict):
    success: bool
    data: list[dict[str, Any]]
    pagination: dict[str, Any]


class ErrorResponse(TypedDict):
    error: str


class SuccessMessageResponse(TypedDict):
    success: bool
    message: str


# Field constants for better type safety and maintainability
class AdSetFields:
    """Ad Set field constants using SDK Field enums."""

    BASIC_FIELDS = [
        AdSet.Field.id,
        AdSet.Field.name,
        AdSet.Field.status,
        AdSet.Field.configured_status,
        AdSet.Field.effective_status,
        AdSet.Field.campaign_id,
        AdSet.Field.daily_budget,
        AdSet.Field.lifetime_budget,
        AdSet.Field.start_time,
        AdSet.Field.end_time,
        AdSet.Field.targeting,
        AdSet.Field.optimization_goal,
        AdSet.Field.billing_event,
        AdSet.Field.bid_amount,
        AdSet.Field.bid_strategy,
        AdSet.Field.created_time,
        AdSet.Field.updated_time,
        AdSet.Field.budget_remaining,
        AdSet.Field.learning_stage_info,
    ]

    DETAILED_FIELDS = BASIC_FIELDS + [
        AdSet.Field.account_id,
        AdSet.Field.promoted_object,
        AdSet.Field.attribution_spec,
    ]

    UPDATE_FIELDS = [
        AdSet.Field.id,
        AdSet.Field.name,
        AdSet.Field.status,
        AdSet.Field.configured_status,
        AdSet.Field.effective_status,
        AdSet.Field.daily_budget,
        AdSet.Field.lifetime_budget,
        AdSet.Field.bid_amount,
        AdSet.Field.targeting,
        AdSet.Field.updated_time,
    ]


adset_server = FastMCP(
    name="FacebookAdSet",
    instructions="Facebook Ad Set management server providing tools for ad set operations.",
)


@adset_server.tool
def get_campaign_adsets(
    campaign_id: str, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get ad sets for a campaign.

    Args:
        campaign_id: Campaign ID
        limit: Maximum number of ad sets to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of ad sets with comprehensive fields and pagination info
    """
    try:
        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        campaign = Campaign(campaign_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        adsets_cursor = campaign.get_ad_sets(
            fields=AdSetFields.BASIC_FIELDS,
            params=params,
        )

        adsets_list = [dict(adset) for adset in adsets_cursor]
        pagination_info = extract_pagination_info(adsets_cursor)

        return {"success": True, "data": adsets_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@adset_server.tool
def get_adset(adset_id: str) -> AdSetResponse | ErrorResponse:
    """Get detailed ad set information.

    Args:
        adset_id: Ad Set ID

    Returns:
        Detailed ad set information
    """
    try:
        adset = AdSet(adset_id)
        adset_data = adset.api_get(fields=AdSetFields.DETAILED_FIELDS)

        return {"success": True, "data": dict(adset_data)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@adset_server.tool
def create_adset(
    campaign_id: str,
    name: str,
    optimization_goal: str,
    billing_event: str,
    bid_amount: int,
    targeting: dict[str, Any],
    status: str = AdSet.ConfiguredStatus.paused,
    daily_budget: int | None = None,
    lifetime_budget: int | None = None,
    start_time: str | None = None,
    end_time: str | None = None,
    promoted_object: dict[str, Any] | None = None,
) -> AdSetResponse | ErrorResponse:
    """Create a new ad set.

    Args:
        campaign_id: Campaign ID
        name: Ad set name
        optimization_goal: Optimization goal (use AdSet.OptimizationGoal constants)
        billing_event: Billing event (use AdSet.BillingEvent constants)
        bid_amount: Bid amount in cents
        targeting: Targeting specification
        status: Ad set status (default: PAUSED)
        daily_budget: Daily budget in cents
        lifetime_budget: Lifetime budget in cents
        start_time: Start time in ISO format
        end_time: End time in ISO format
        promoted_object: Promoted object specification

    Returns:
        Created ad set information
    """
    try:
        campaign = Campaign(campaign_id)

        params = {
            AdSet.Field.name: name,
            AdSet.Field.optimization_goal: optimization_goal,
            AdSet.Field.billing_event: billing_event,
            AdSet.Field.bid_amount: bid_amount,
            AdSet.Field.targeting: targeting,
            AdSet.Field.configured_status: status,
        }

        if daily_budget is not None:
            params[AdSet.Field.daily_budget] = daily_budget
        if lifetime_budget is not None:
            params[AdSet.Field.lifetime_budget] = lifetime_budget
        if start_time is not None:
            params[AdSet.Field.start_time] = start_time
        if end_time is not None:
            params[AdSet.Field.end_time] = end_time
        if promoted_object is not None:
            params[AdSet.Field.promoted_object] = promoted_object

        adset = campaign.create_ad_set(fields=[], params=params)

        return {"success": True, "data": dict(adset)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@adset_server.tool
def update_adset(
    adset_id: str,
    name: str | None = None,
    status: str | None = None,
    daily_budget: int | None = None,
    lifetime_budget: int | None = None,
    bid_amount: int | None = None,
    targeting: dict[str, Any] | None = None,
    start_time: str | None = None,
    end_time: str | None = None,
) -> AdSetResponse | ErrorResponse:
    """Update an existing ad set.

    Args:
        adset_id: Ad Set ID
        name: New ad set name
        status: New ad set status
        daily_budget: New daily budget in cents
        lifetime_budget: New lifetime budget in cents
        bid_amount: New bid amount in cents
        targeting: New targeting specification
        start_time: New start time in ISO format
        end_time: New end time in ISO format

    Returns:
        Updated ad set information
    """
    try:
        adset = AdSet(adset_id)

        params = {}
        if name is not None:
            params[AdSet.Field.name] = name
        if status is not None:
            params[AdSet.Field.configured_status] = status
        if daily_budget is not None:
            params[AdSet.Field.daily_budget] = daily_budget
        if lifetime_budget is not None:
            params[AdSet.Field.lifetime_budget] = lifetime_budget
        if bid_amount is not None:
            params[AdSet.Field.bid_amount] = bid_amount
        if targeting is not None:
            params[AdSet.Field.targeting] = targeting
        if start_time is not None:
            params[AdSet.Field.start_time] = start_time
        if end_time is not None:
            params[AdSet.Field.end_time] = end_time

        if not params:
            return {"error": "No parameters provided for update"}

        adset.api_update(fields=[], params=params)

        # Get updated ad set data
        updated_adset = adset.api_get(fields=AdSetFields.UPDATE_FIELDS)

        return {"success": True, "data": dict(updated_adset)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@adset_server.tool
def delete_adset(adset_id: str) -> SuccessMessageResponse | ErrorResponse:
    """Delete an ad set.

    Args:
        adset_id: Ad Set ID

    Returns:
        Deletion confirmation
    """
    try:
        adset = AdSet(adset_id)
        adset.api_delete()

        return {"success": True, "message": f"Ad set {adset_id} deleted successfully"}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
