"""Insights MCP Server using Facebook Business SDK."""

from typing import Any, TypedDict

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.campaign import Campaign
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from ..config import format_account_id, resolve_account_id


class InsightsResponse(TypedDict):
    success: bool
    data: list[dict[str, Any]] | dict[str, Any]


class PaginatedInsightsResponse(TypedDict):
    success: bool
    data: list[dict[str, Any]]
    pagination: dict[str, Any]


class ErrorResponse(TypedDict):
    error: str


# Field constants for better type safety and maintainability
class InsightsFields:
    """Insights field constants using SDK Field enums."""

    BASIC_FIELDS = [
        AdsInsights.Field.impressions,
        AdsInsights.Field.clicks,
        AdsInsights.Field.spend,
        AdsInsights.Field.reach,
        AdsInsights.Field.frequency,
        AdsInsights.Field.cpm,
        AdsInsights.Field.cpc,
        AdsInsights.Field.ctr,
        AdsInsights.Field.conversions,
        AdsInsights.Field.cost_per_conversion,
        AdsInsights.Field.date_start,
        AdsInsights.Field.date_stop,
    ]

    CAMPAIGN_FIELDS = [
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
    ] + BASIC_FIELDS

    ADSET_FIELDS = [
        AdsInsights.Field.adset_id,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
    ] + BASIC_FIELDS

    AD_FIELDS = [
        AdsInsights.Field.ad_id,
        AdsInsights.Field.ad_name,
        AdsInsights.Field.adset_id,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
    ] + BASIC_FIELDS


insights_server = FastMCP(
    name="FacebookInsights",
    instructions="Facebook Insights server providing tools for performance data and analytics.",
)


@insights_server.tool
def get_account_insights(
    account_id: str | None = None,
    time_range: dict[str, str] | None = None,
    fields: list[str] | None = None,
    breakdowns: list[str] | None = None,
    limit: int = 25,
    after: str | None = None,
) -> PaginatedInsightsResponse | ErrorResponse:
    """Get insights for an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        time_range: Time range dict with 'since' and 'until' keys (YYYY-MM-DD format)
        fields: List of insight fields to retrieve
        breakdowns: List of breakdown dimensions
        limit: Maximum number of insights to return (max 100)
        after: Pagination cursor for next page

    Returns:
        Account insights data and pagination info
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        account = AdAccount(account_id)

        # Default fields if none provided
        if fields is None:
            fields = InsightsFields.BASIC_FIELDS

        params = {"limit": limit}
        if time_range:
            params["time_range"] = time_range
        if breakdowns:
            params["breakdowns"] = breakdowns
        if after:
            params["after"] = after

        insights_cursor = account.get_insights(fields=fields, params=params)

        insights_list = [dict(insight) for insight in insights_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(insights_cursor, "_finished_iteration")
            and not insights_cursor._finished_iteration
        ):
            if hasattr(insights_cursor, "params") and "after" in insights_cursor.params:
                pagination_info["next_cursor"] = insights_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": insights_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@insights_server.tool
def get_campaign_insights(
    campaign_id: str,
    time_range: dict[str, str] | None = None,
    fields: list[str] | None = None,
    breakdowns: list[str] | None = None,
    limit: int = 25,
    after: str | None = None,
) -> PaginatedInsightsResponse | ErrorResponse:
    """Get insights for a campaign.

    Args:
        campaign_id: Campaign ID
        time_range: Time range dict with 'since' and 'until' keys (YYYY-MM-DD format)
        fields: List of insight fields to retrieve
        breakdowns: List of breakdown dimensions
        limit: Maximum number of insights to return (max 100)
        after: Pagination cursor for next page

    Returns:
        Campaign insights data and pagination info
    """
    try:
        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        campaign = Campaign(campaign_id)

        # Default fields if none provided
        if fields is None:
            fields = InsightsFields.CAMPAIGN_FIELDS

        params = {"limit": limit}
        if time_range:
            params["time_range"] = time_range
        if breakdowns:
            params["breakdowns"] = breakdowns
        if after:
            params["after"] = after

        insights_cursor = campaign.get_insights(fields=fields, params=params)

        insights_list = [dict(insight) for insight in insights_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(insights_cursor, "_finished_iteration")
            and not insights_cursor._finished_iteration
        ):
            if hasattr(insights_cursor, "params") and "after" in insights_cursor.params:
                pagination_info["next_cursor"] = insights_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": insights_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@insights_server.tool
def get_adset_insights(
    adset_id: str,
    time_range: dict[str, str] | None = None,
    fields: list[str] | None = None,
    breakdowns: list[str] | None = None,
    limit: int = 25,
    after: str | None = None,
) -> PaginatedInsightsResponse | ErrorResponse:
    """Get insights for an ad set.

    Args:
        adset_id: Ad Set ID
        time_range: Time range dict with 'since' and 'until' keys (YYYY-MM-DD format)
        fields: List of insight fields to retrieve
        breakdowns: List of breakdown dimensions
        limit: Maximum number of insights to return (max 100)
        after: Pagination cursor for next page

    Returns:
        Ad set insights data and pagination info
    """
    try:
        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        adset = AdSet(adset_id)

        # Default fields if none provided
        if fields is None:
            fields = InsightsFields.ADSET_FIELDS

        params = {"limit": limit}
        if time_range:
            params["time_range"] = time_range
        if breakdowns:
            params["breakdowns"] = breakdowns
        if after:
            params["after"] = after

        insights_cursor = adset.get_insights(fields=fields, params=params)

        insights_list = [dict(insight) for insight in insights_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(insights_cursor, "_finished_iteration")
            and not insights_cursor._finished_iteration
        ):
            if hasattr(insights_cursor, "params") and "after" in insights_cursor.params:
                pagination_info["next_cursor"] = insights_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": insights_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@insights_server.tool
def get_ad_insights(
    ad_id: str,
    time_range: dict[str, str] | None = None,
    fields: list[str] | None = None,
    breakdowns: list[str] | None = None,
    limit: int = 25,
    after: str | None = None,
) -> PaginatedInsightsResponse | ErrorResponse:
    """Get insights for an ad.

    Args:
        ad_id: Ad ID
        time_range: Time range dict with 'since' and 'until' keys (YYYY-MM-DD format)
        fields: List of insight fields to retrieve
        breakdowns: List of breakdown dimensions
        limit: Maximum number of insights to return (max 100)
        after: Pagination cursor for next page

    Returns:
        Ad insights data and pagination info
    """
    try:
        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        ad = Ad(ad_id)

        # Default fields if none provided
        if fields is None:
            fields = InsightsFields.AD_FIELDS

        params = {"limit": limit}
        if time_range:
            params["time_range"] = time_range
        if breakdowns:
            params["breakdowns"] = breakdowns
        if after:
            params["after"] = after

        insights_cursor = ad.get_insights(fields=fields, params=params)

        insights_list = [dict(insight) for insight in insights_cursor]

        # Extract pagination info
        pagination_info = {}
        if (
            hasattr(insights_cursor, "_finished_iteration")
            and not insights_cursor._finished_iteration
        ):
            if hasattr(insights_cursor, "params") and "after" in insights_cursor.params:
                pagination_info["next_cursor"] = insights_cursor.params["after"]
                pagination_info["has_next_page"] = True
            else:
                pagination_info["has_next_page"] = False
        else:
            pagination_info["has_next_page"] = False

        return {"success": True, "data": insights_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@insights_server.tool
def get_insights_async(
    level: str,
    object_id: str,
    time_range: dict[str, str] | None = None,
    fields: list[str] | None = None,
    breakdowns: list[str] | None = None,
) -> InsightsResponse | ErrorResponse:
    """Get insights asynchronously for large data sets.

    Args:
        level: Level of insights ('account', 'campaign', 'adset', 'ad')
        object_id: ID of the object to get insights for
        time_range: Time range dict with 'since' and 'until' keys (YYYY-MM-DD format)
        fields: List of insight fields to retrieve
        breakdowns: List of breakdown dimensions

    Returns:
        Async job information
    """
    try:
        if level == "account":
            account_id = format_account_id(object_id)
            obj = AdAccount(account_id)
        elif level == "campaign":
            obj = Campaign(object_id)
        elif level == "adset":
            obj = AdSet(object_id)
        elif level == "ad":
            obj = Ad(object_id)
        else:
            return {
                "error": f"Invalid level: {level}. Must be one of: account, campaign, adset, ad"
            }

        # Default fields if none provided
        if fields is None:
            fields = InsightsFields.BASIC_FIELDS

        params = {"level": level}
        if time_range:
            params["time_range"] = time_range
        if breakdowns:
            params["breakdowns"] = breakdowns

        async_job = obj.get_insights_async(fields=fields, params=params)

        return {"success": True, "data": {"job_id": async_job.get_id(), "status": "submitted"}}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
