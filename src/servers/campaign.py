"""Campaign MCP Server using Facebook Business SDK."""

from typing import Any, TypedDict

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from ..config import resolve_account_id


class CampaignResponse(TypedDict):
    success: bool
    data: dict[str, Any] | list[dict[str, Any]]


class ErrorResponse(TypedDict):
    error: str


class SuccessMessageResponse(TypedDict):
    success: bool
    message: str


# Field constants for better type safety and maintainability
class CampaignFields:
    """Campaign field constants using SDK Field enums."""

    BASIC_FIELDS = [
        Campaign.Field.id,
        Campaign.Field.name,
        Campaign.Field.status,
        Campaign.Field.configured_status,
        Campaign.Field.effective_status,
        Campaign.Field.objective,
        Campaign.Field.daily_budget,
        Campaign.Field.lifetime_budget,
        Campaign.Field.start_time,
        Campaign.Field.stop_time,
        Campaign.Field.created_time,
        Campaign.Field.updated_time,
        Campaign.Field.account_id,
        Campaign.Field.buying_type,
        Campaign.Field.spend_cap,
        Campaign.Field.budget_remaining,
    ]

    DETAILED_FIELDS = BASIC_FIELDS + [
        Campaign.Field.bid_strategy,
        Campaign.Field.promoted_object,
        Campaign.Field.special_ad_categories,
    ]

    UPDATE_FIELDS = [
        Campaign.Field.id,
        Campaign.Field.name,
        Campaign.Field.status,
        Campaign.Field.configured_status,
        Campaign.Field.effective_status,
        Campaign.Field.objective,
        Campaign.Field.daily_budget,
        Campaign.Field.lifetime_budget,
        Campaign.Field.start_time,
        Campaign.Field.stop_time,
        Campaign.Field.updated_time,
    ]


campaign_server = FastMCP(
    name="FacebookCampaign",
    instructions="Facebook Campaign management server providing tools for campaign operations.",
)


@campaign_server.tool
def get_campaigns(
    account_id: str | None = None, limit: int = 25
) -> CampaignResponse | ErrorResponse:
    """Get campaigns for an ad account.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        limit: Maximum number of campaigns to return

    Returns:
        List of campaigns with comprehensive fields
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        account = AdAccount(account_id)
        campaigns = account.get_campaigns(
            fields=CampaignFields.BASIC_FIELDS,
            params={"limit": limit},
        )

        campaigns_list = [dict(campaign) for campaign in campaigns]
        return {"success": True, "data": campaigns_list}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@campaign_server.tool
def get_campaign(campaign_id: str) -> CampaignResponse | ErrorResponse:
    """Get detailed campaign information.

    Args:
        campaign_id: Campaign ID

    Returns:
        Detailed campaign information
    """
    try:
        campaign = Campaign(campaign_id)
        campaign_data = campaign.api_get(fields=CampaignFields.DETAILED_FIELDS)

        return {"success": True, "data": dict(campaign_data)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@campaign_server.tool
def create_campaign(
    account_id: str | None,
    name: str,
    objective: str,
    status: str = Campaign.ConfiguredStatus.paused,
    daily_budget: int | None = None,
    lifetime_budget: int | None = None,
    start_time: str | None = None,
    stop_time: str | None = None,
    special_ad_categories: list[str] | None = None,
) -> CampaignResponse | ErrorResponse:
    """Create a new campaign.

    Args:
        account_id: Ad account ID (optional, uses default from env if not provided)
        name: Campaign name
        objective: Campaign objective (use Campaign.Objective constants)
        status: Campaign status (default: PAUSED)
        daily_budget: Daily budget in cents
        lifetime_budget: Lifetime budget in cents
        start_time: Start time in ISO format
        stop_time: Stop time in ISO format
        special_ad_categories: Special ad categories if applicable

    Returns:
        Created campaign information
    """
    try:
        account_id, error = resolve_account_id(account_id)
        if error:
            return {"error": error}

        account = AdAccount(account_id)

        params = {
            Campaign.Field.name: name,
            Campaign.Field.objective: objective,
            Campaign.Field.configured_status: status,
        }

        if daily_budget is not None:
            params[Campaign.Field.daily_budget] = daily_budget
        if lifetime_budget is not None:
            params[Campaign.Field.lifetime_budget] = lifetime_budget
        if start_time is not None:
            params[Campaign.Field.start_time] = start_time
        if stop_time is not None:
            params[Campaign.Field.stop_time] = stop_time
        if special_ad_categories is not None:
            params[Campaign.Field.special_ad_categories] = special_ad_categories

        campaign = account.create_campaign(fields=[], params=params)

        return {"success": True, "data": dict(campaign)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@campaign_server.tool
def update_campaign(
    campaign_id: str,
    name: str | None = None,
    status: str | None = None,
    daily_budget: int | None = None,
    lifetime_budget: int | None = None,
    start_time: str | None = None,
    stop_time: str | None = None,
) -> CampaignResponse | ErrorResponse:
    """Update an existing campaign.

    Args:
        campaign_id: Campaign ID
        name: New campaign name
        status: New campaign status
        daily_budget: New daily budget in cents
        lifetime_budget: New lifetime budget in cents
        start_time: New start time in ISO format
        stop_time: New stop time in ISO format

    Returns:
        Updated campaign information
    """
    try:
        campaign = Campaign(campaign_id)

        params = {}
        if name is not None:
            params[Campaign.Field.name] = name
        if status is not None:
            params[Campaign.Field.configured_status] = status
        if daily_budget is not None:
            params[Campaign.Field.daily_budget] = daily_budget
        if lifetime_budget is not None:
            params[Campaign.Field.lifetime_budget] = lifetime_budget
        if start_time is not None:
            params[Campaign.Field.start_time] = start_time
        if stop_time is not None:
            params[Campaign.Field.stop_time] = stop_time

        if not params:
            return {"error": "No parameters provided for update"}

        campaign.api_update(fields=[], params=params)

        # Get updated campaign data
        updated_campaign = campaign.api_get(fields=CampaignFields.UPDATE_FIELDS)

        return {"success": True, "data": dict(updated_campaign)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@campaign_server.tool
def delete_campaign(campaign_id: str) -> SuccessMessageResponse | ErrorResponse:
    """Delete a campaign.

    Args:
        campaign_id: Campaign ID

    Returns:
        Deletion confirmation
    """
    try:
        campaign = Campaign(campaign_id)
        campaign.api_delete()

        return {"success": True, "message": f"Campaign {campaign_id} deleted successfully"}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
