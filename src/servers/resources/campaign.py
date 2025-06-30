"""Streamlined Campaign MCP Server - Core Operations Only."""

from typing import Any

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCampaign"
instructions = """
Campaign MCP Server for Facebook Business API - Core Operations.

For common workflows, use the universal server or workflow servers.
This server provides essential operations that handle 80% of use cases.

Use `run_any_campaign_fn` for any operations not covered here.
"""

campaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_campaign(
    campaign_id: str,
    fields: list[str] = [],
) -> str:
    """Get a Campaign object by ID.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields include:
            - name: Campaign name
            - status: Current status (ACTIVE, PAUSED, DELETED, ARCHIVED)
            - effective_status: Actual running status considering all factors
            - objective: Campaign objective (see CampaignObjective enum)
            - daily_budget: Daily budget in cents
            - lifetime_budget: Lifetime budget in cents
            - spend_cap: Total spending limit
            - created_time: When campaign was created
            - start_time/stop_time: Campaign schedule
            See CampaignFields for all available fields.
    """
    return Campaign(campaign_id).api_get(fields=fields)


@wrapped_fn_tool
def update_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Update a Campaign object.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to return after update.
        params: Parameters to update. Common updates:
            - name: Change campaign name
            - status: ACTIVE or PAUSED (see CampaignStatus enum)
            - daily_budget: Update daily budget in cents
            - lifetime_budget: Update lifetime budget in cents
            - spend_cap: Update total spending limit
            - bid_strategy: Change bidding strategy
            Note: Some fields like objective cannot be changed after creation.
    """
    return Campaign(campaign_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaign(
    campaign_id: str,
) -> str:
    """Delete a Campaign.

    Args:
        campaign_id: The ID of the Campaign to delete.
    """
    return Campaign(campaign_id).api_delete()


# ---- Child Resource Access (2) ----
@wrapped_fn_tool
def get_ad_sets(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get ad sets for this campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve (e.g., ['name', 'status', 'daily_budget']).
        params: Query parameters (e.g., {'limit': 100, 'effective_status': ['ACTIVE']}).
    """
    return Campaign(campaign_id).get_ad_sets(fields=fields, params=params)


@wrapped_fn_tool
def get_ads(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get ads for this campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve (e.g., ['name', 'status', 'creative']).
        params: Query parameters (e.g., {'limit': 100, 'effective_status': ['ACTIVE']}).
    """
    return Campaign(campaign_id).get_ads(fields=fields, params=params)


# ---- Performance Analysis (2) ----
@wrapped_fn_tool
def get_insights(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights (performance data) for this campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Metrics to retrieve. Common metrics:
            - impressions: Number of times ads were shown
            - reach: Unique people who saw ads
            - clicks: Total clicks
            - spend: Amount spent
            - cpm: Cost per 1000 impressions
            - cpp: Cost per 1000 people reached
            - ctr: Click-through rate
            - conversions: Conversion events
            - cost_per_conversion: Average conversion cost
        params: Query parameters:
            - date_preset: last_7d, last_30d, lifetime (see CampaignDatePreset)
            - breakdowns: ['age', 'gender', 'placement', 'device_platform']
            - time_increment: 1, 7, or 'monthly' for time series data
    """
    return Campaign(campaign_id).get_insights(fields=fields, params=params)


@wrapped_fn_tool
def get_insights_async(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights asynchronously for large data requests.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Metrics to retrieve.
        params: Query parameters (use for large date ranges or detailed breakdowns).
    """
    return Campaign(campaign_id).get_insights_async(fields=fields, params=params)


# ---- Dynamic Fallback (1) ----
@wrapped_fn_tool
def run_any_campaign_fn(
    campaign_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically call any method on the Campaign object.

    Use this for operations not covered by the core tools above.
    Example: run_any_campaign_fn('123', 'get_ad_studies', [], {'limit': 10})

    Args:
        campaign_id: The ID of the Campaign.
        fn: Method name to call on Campaign object.
        args: Positional arguments for the method.
        kwargs: Keyword arguments for the method.
    """
    campaign = Campaign(campaign_id)
    if not hasattr(campaign, fn):
        return (
            f"Campaign does not have method '{fn}'. Check the Facebook Business SDK documentation."
        )
    f = getattr(campaign, fn)
    if not callable(f):
        return f"{fn} is not a callable method on Campaign."
    return str(f(*args, **kwargs))


# ---- Register tools ----
campaign_server.tool(get_campaign)
campaign_server.tool(update_campaign)
campaign_server.tool(delete_campaign)
campaign_server.tool(get_ad_sets)
campaign_server.tool(get_ads)
campaign_server.tool(get_insights)
campaign_server.tool(get_insights_async)
campaign_server.tool(run_any_campaign_fn)
