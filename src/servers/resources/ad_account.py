"""Streamlined Ad Account MCP Server - Core Operations Only."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.generated.models.adaccount import AdAccountField
from src.generated.models.campaign import CampaignField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccount"
instructions = """
Ad Account MCP Server for Facebook Business API - Core Operations.

For common workflows, use the universal server or workflow servers.
This server provides essential operations that handle 80% of use cases.

Use `run_any_ad_account_fn` for any operations not covered here.
"""

ad_account_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@wrapped_fn_tool
def get_ad_account(
    ad_account_id: str,
    fields: list[AdAccountField] = [],
) -> str:
    """Get an AdAccount object by ID.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to retrieve. Available fields include:
            - name: Account name
            - account_status: 1 = active, 2 = disabled, 3 = unsettled
            - currency: Three letter currency code (e.g., 'USD', 'EUR')
            - balance: Current balance in account currency
            - spend_cap: Account spending limit
            - timezone_name: Business timezone
            - created_time: When the account was created
            See AdAccountFields for all available fields.
    """
    account = AdAccount(ad_account_id)
    return account.api_get(fields=fields)


@wrapped_fn_tool
def update_ad_account(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Update an AdAccount object.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to return after update.
        params: Parameters to update (e.g., {'name': 'New Name'}).
    """
    return AdAccount(ad_account_id).api_update(fields=fields, params=params)


# ---- Resource Management (4) ----
@wrapped_fn_tool
def get_campaigns(
    ad_account_id: str,
    fields: list[CampaignField] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get campaigns for this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to retrieve (e.g., ['name', 'status', 'objective']).
        params: Query parameters (e.g., {'limit': 100, 'effective_status': ['ACTIVE']}).
    """
    return AdAccount(ad_account_id).get_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def create_campaign(
    ad_account_id: str,
    fields: list[CampaignField] = [],
    params: dict[str, Any] = {},
) -> str:
    """Create a new campaign in this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to return for created campaign.
        params: Campaign creation parameters. Required fields:
            - name: Campaign name
            - objective: Campaign objective (see CampaignObjective enum)
              Options: LINK_CLICKS, CONVERSIONS, BRAND_AWARENESS, REACH, etc.
            - status: ACTIVE or PAUSED (start paused recommended)
            Optional fields:
            - special_ad_categories: ['NONE'] or ['HOUSING', 'EMPLOYMENT', 'CREDIT']
            - daily_budget: Daily budget in cents
            - lifetime_budget: Lifetime budget in cents
            - bid_strategy: LOWEST_COST_WITHOUT_CAP (default) or COST_CAP
    """
    return AdAccount(ad_account_id).create_campaign(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_sets(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get ad sets for this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to retrieve (e.g., ['name', 'status', 'daily_budget']).
        params: Query parameters (e.g., {'limit': 100, 'effective_status': ['ACTIVE']}).
    """
    return AdAccount(ad_account_id).get_ad_sets(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_set(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Create a new ad set in this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to return for created ad set.
        params: Ad set creation parameters. Required fields:
            - name: Ad set name
            - campaign_id: Parent campaign ID
            - daily_budget or lifetime_budget: Budget in cents (e.g., 10000 = $100)
            - billing_event: IMPRESSIONS, CLICKS, or other (see AdSetBillingEvent)
            - optimization_goal: What to optimize for (see AdSetOptimizationGoal)
              Common: REACH, IMPRESSIONS, LINK_CLICKS, CONVERSIONS, VALUE
            - targeting: Targeting spec dict with geo_locations, age_min/max, etc.
            - status: ACTIVE or PAUSED (start paused recommended)
            Optional fields:
            - start_time/end_time: Schedule as datetime strings
            - bid_amount: Manual bid in cents (if not using auto-bidding)
    """
    return AdAccount(ad_account_id).create_ad_set(fields=fields, params=params)


# ---- Insights & Reporting (2) ----
@wrapped_fn_tool
def get_insights(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights (performance data) for this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Metrics to retrieve. Common metrics:
            - impressions: Number of times ads were shown
            - clicks: Total clicks (all click types)
            - spend: Amount spent in account currency
            - cpm: Cost per 1000 impressions
            - cpc: Cost per click
            - ctr: Click-through rate percentage
            - conversions: Number of conversions
            - cost_per_conversion: Average cost per conversion
        params: Query parameters:
            - date_preset: Time range (last_7d, last_30d, this_month, etc.)
            - time_range: Custom range {'since': 'YYYY-MM-DD', 'until': 'YYYY-MM-DD'}
            - level: Aggregation level (account, campaign, adset, ad)
            - breakdowns: Dimensions to split by (age, gender, placement, etc.)
    """
    return AdAccount(ad_account_id).get_insights(fields=fields, params=params)


@wrapped_fn_tool
def get_insights_async(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights asynchronously for large data requests.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Metrics to retrieve.
        params: Query parameters (use for large date ranges or detailed breakdowns).
    """
    return AdAccount(ad_account_id).get_insights_async(fields=fields, params=params)


# ---- Targeting & Audiences (2) ----
@wrapped_fn_tool
def get_custom_audiences(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get custom audiences for this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to retrieve (e.g., ['name', 'description', 'approximate_count']).
        params: Query parameters (e.g., {'limit': 100}).
    """
    return AdAccount(ad_account_id).get_custom_audiences(fields=fields, params=params)


@wrapped_fn_tool
def create_custom_audience(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Create a new custom audience in this ad account.

    Args:
        ad_account_id: The ID of the Ad Account (must start with 'act_').
        fields: Fields to return for created audience.
        params: Audience creation parameters (e.g., {'name': 'My Audience', 'subtype': 'CUSTOM', 'description': 'Description', 'customer_file_source': 'USER_PROVIDED_ONLY'}).
    """
    return AdAccount(ad_account_id).create_custom_audience(fields=fields, params=params)


# ---- Dynamic Fallback (1) ----
@wrapped_fn_tool
def run_any_ad_account_fn(
    account_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically call any method on the AdAccount object.

    Use this for operations not covered by the core tools above.
    Example: run_any_ad_account_fn('act_123', 'get_targeting_browse', [], {'limit': 10})

    Args:
        account_id: The ID of the Ad Account (must start with 'act_').
        fn: Method name to call on AdAccount object.
        args: Positional arguments for the method.
        kwargs: Keyword arguments for the method.
    """
    account = AdAccount(account_id)
    if not hasattr(account, fn):
        return (
            f"AdAccount does not have method '{fn}'. Check the Facebook Business SDK documentation."
        )
    f = getattr(account, fn)
    if not callable(f):
        return f"{fn} is not a callable method on AdAccount."
    return str(f(*args, **kwargs))


# ---- Register tools ----
ad_account_server.tool(get_ad_account)
ad_account_server.tool(update_ad_account)
ad_account_server.tool(get_campaigns)
ad_account_server.tool(create_campaign)
ad_account_server.tool(get_ad_sets)
ad_account_server.tool(create_ad_set)
ad_account_server.tool(get_insights)
ad_account_server.tool(get_insights_async)
ad_account_server.tool(get_custom_audiences)
ad_account_server.tool(create_custom_audience)
ad_account_server.tool(run_any_ad_account_fn)
