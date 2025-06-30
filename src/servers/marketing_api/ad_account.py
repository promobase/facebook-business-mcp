"""Simplified Ad Account MCP Server using Facebook Business SDK."""

import inspect
from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.utils import (
    list_callable_methods,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookAdAccount"
instructions = """
This is the AdAccount MCP Server for managing Facebook Ad Accounts. 

QUICK START - Use these workflow tools for common tasks:
1. `get_account_structure_overview` - See what's in the account
2. `create_complete_campaign` - Simple campaign creation
3. `create_traffic_campaign_workflow` - Complete traffic campaign with targeting
4. `create_conversion_campaign_workflow` - Conversion campaign with pixel setup
5. `get_active_campaigns_with_performance` - Monitor active campaigns

For advanced operations:
- Use `get_usage_on_ad_account` to see all available methods
- Use `run_any_ad_account_fn` to call any AdAccount method directly
- Individual tools are available for granular control
"""

ad_account_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Core API methods ----
@wrapped_fn_tool
def get_ad_account(
    ad_account_id: str,
    fields: list[str] = [],
) -> str:
    account = AdAccount(ad_account_id)
    return account.api_get(fields=fields)


@wrapped_fn_tool
def update_ad_account(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).api_update(fields=fields, params=params)


#  ---- Campaign management ----
@wrapped_fn_tool
def get_campaigns(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def create_campaign(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_campaign(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaigns(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def get_campaigns_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_campaigns_by_labels(fields=fields, params=params)


#  ---- Ad Set management ----
@wrapped_fn_tool
def get_ad_sets(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_sets(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_set(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_set(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_sets_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_sets_by_labels(fields=fields, params=params)


#  ---- Ad management ----
@wrapped_fn_tool
def get_ads(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads(fields=fields, params=params)


@wrapped_fn_tool
def create_ad(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad(fields=fields, params=params)


@wrapped_fn_tool
def get_ads_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads_by_labels(fields=fields, params=params)


#  ---- Creative management ----
@wrapped_fn_tool
def get_ad_creatives(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_creatives(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_creative(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_creatives_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_creatives_by_labels(fields=fields, params=params)


#  ---- Image management ----
@wrapped_fn_tool
def get_ad_images(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_images(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_image(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_image(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad_images(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_ad_images(fields=fields, params=params)


#  ---- Video management ----
@wrapped_fn_tool
def get_ad_videos(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_videos(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_video(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_video(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad_videos(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_ad_videos(fields=fields, params=params)


#  ---- Custom Audience management ----
@wrapped_fn_tool
def get_custom_audiences(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_custom_audiences(fields=fields, params=params)


@wrapped_fn_tool
def create_custom_audience(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_custom_audience(fields=fields, params=params)


#  ---- Insights and reporting ----
@wrapped_fn_tool
def get_insights(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    is_async: bool = False,
) -> str:
    return AdAccount(ad_account_id).get_insights(fields=fields, params=params, is_async=is_async)


@wrapped_fn_tool
def get_insights_async(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_insights_async(fields=fields, params=params)


#  ---- Targeting tools ----
@wrapped_fn_tool
def get_targeting_browse(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_browse(fields=fields, params=params)


@wrapped_fn_tool
def get_targeting_search(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_search(fields=fields, params=params)


@wrapped_fn_tool
def get_targeting_suggestions(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_suggestions(fields=fields, params=params)


@wrapped_fn_tool
def get_reach_estimate(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_reach_estimate(fields=fields, params=params)


@wrapped_fn_tool
def get_delivery_estimate(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_delivery_estimate(fields=fields, params=params)


#  ---- Pixel management ----
@wrapped_fn_tool
def get_ads_pixels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads_pixels(fields=fields, params=params)


@wrapped_fn_tool
def create_ads_pixel(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ads_pixel(fields=fields, params=params)


#  ---- User management ----
@wrapped_fn_tool
def get_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_users(fields=fields, params=params)


@wrapped_fn_tool
def get_assigned_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_assigned_users(fields=fields, params=params)


@wrapped_fn_tool
def create_assigned_user(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_assigned_user(fields=fields, params=params)


@wrapped_fn_tool
def delete_assigned_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_assigned_users(fields=fields, params=params)


# ---- dynamic tools ----
@wrapped_fn_tool
def get_usage_on_ad_account(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use the tools and methods available. This includes examples.
    Optionally, you can pass in a metod name and you will see the src code for usage of that method.
    """
    field_enum_info: dict = AdAccount._get_field_enum_info()
    methods = list_callable_methods(AdAccount)

    usage = f"""
    This is the AdAccount wrapper on Facebook Business Python SDK. 
    You can use the {run_any_ad_account_fn.__name__} tool to call any methods, here is the docstring for it: {run_any_ad_account_fn.__doc__}

    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {AdAccount._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    account = AdAccount(..)
    account.get_campaigns(fields=[..], params=..) // get campaigns
    account.get_ads(fields=[..], params=..) // get ads
    """

    if fn:
        # append method src
        if hasattr(AdAccount, fn):
            method = getattr(AdAccount, fn)
            if callable(method):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{fn} is not a callable method on AdAccount."
    return usage


@wrapped_fn_tool
def run_any_ad_account_fn(
    account_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically calls a method on the AdAccount object.
    takes in an account_id, method name (fn), and optional args/kwargs.
    it will be called like this:
    ```account = AdAccount(account_id)
    result = getattr(account, fn)(*args, **kwargs)
    ```
    """
    account = AdAccount(account_id)
    if not hasattr(account, fn):
        return f"AdAccount does not have method '{fn}'. use the {get_usage_on_ad_account.__name__} tool to see available methods & usage."
    f = getattr(account, fn)
    if not callable(f):
        return f"{fn} is not a callable method on AdAccount."
    return str(f(*args, **kwargs))


#  ---- Higher-level workflow tools ----
@wrapped_fn_tool
def create_complete_campaign(
    ad_account_id: str,
    campaign_name: str,
    objective: str,
    daily_budget: int,
    special_ad_categories: list[str] = [],
) -> str:
    """Create a complete campaign with common settings in one call."""
    account = AdAccount(ad_account_id)
    campaign = account.create_campaign(
        fields=[],
        params={
            "name": campaign_name,
            "objective": objective,
            "status": "PAUSED",
            "special_ad_categories": special_ad_categories,
            "daily_budget": daily_budget * 100,  # Convert to cents
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        },
    )
    return campaign


@wrapped_fn_tool
def create_traffic_campaign_workflow(
    ad_account_id: str,
    campaign_name: str,
    daily_budget: int,
    destination_url: str,
    audience_targeting: dict[str, Any] = {},
) -> str:
    """Complete workflow to create a traffic campaign with ad set and targeting."""
    account = AdAccount(ad_account_id)

    # Create campaign
    campaign = account.create_campaign(
        fields=["id"],
        params={
            "name": campaign_name,
            "objective": "LINK_CLICKS",
            "status": "PAUSED",
            "daily_budget": daily_budget * 100,
        },
    )

    # Create ad set with targeting
    default_targeting = {
        "geo_locations": {"countries": ["US"]},
        "age_min": 18,
        "age_max": 65,
    }
    default_targeting.update(audience_targeting)

    adset = account.create_ad_set(
        fields=["id"],
        params={
            "name": f"{campaign_name} - Ad Set",
            "campaign_id": campaign["id"],
            "daily_budget": daily_budget * 100,
            "billing_event": "IMPRESSIONS",
            "optimization_goal": "LINK_CLICKS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
            "targeting": default_targeting,
            "status": "PAUSED",
            "destination_type": "WEBSITE",
            "promoted_object": {"website_url": destination_url},
        },
    )

    return {
        "campaign": campaign,
        "adset": adset,
        "next_step": "Create ad creative and ad using the returned IDs",
    }


@wrapped_fn_tool
def create_conversion_campaign_workflow(
    ad_account_id: str,
    campaign_name: str,
    daily_budget: int,
    pixel_id: str,
    conversion_event: str = "Purchase",
    audience_targeting: dict[str, Any] = {},
) -> str:
    """Complete workflow to create a conversion-optimized campaign."""
    account = AdAccount(ad_account_id)

    # Create campaign
    campaign = account.create_campaign(
        fields=["id"],
        params={
            "name": campaign_name,
            "objective": "CONVERSIONS",
            "status": "PAUSED",
            "daily_budget": daily_budget * 100,
        },
    )

    # Create ad set optimized for conversions
    default_targeting = {
        "geo_locations": {"countries": ["US"]},
        "age_min": 18,
        "age_max": 65,
    }
    default_targeting.update(audience_targeting)

    adset = account.create_ad_set(
        fields=["id"],
        params={
            "name": f"{campaign_name} - Conversion Ad Set",
            "campaign_id": campaign["id"],
            "daily_budget": daily_budget * 100,
            "billing_event": "IMPRESSIONS",
            "optimization_goal": "CONVERSIONS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
            "targeting": default_targeting,
            "status": "PAUSED",
            "promoted_object": {
                "pixel_id": pixel_id,
                "custom_event_type": conversion_event,
            },
        },
    )

    return {
        "campaign": campaign,
        "adset": adset,
        "pixel_id": pixel_id,
        "conversion_event": conversion_event,
        "next_step": "Create ad creative and ad using the returned IDs",
    }


@wrapped_fn_tool
def get_account_structure_overview(
    ad_account_id: str,
    include_insights: bool = False,
) -> str:
    """Get a complete overview of account structure with counts and status."""
    account = AdAccount(ad_account_id)

    # Get account info
    account_info = account.api_get(fields=["name", "account_status", "currency", "timezone_name"])

    # Get campaigns
    campaigns = account.get_campaigns(fields=["name", "status", "objective"], params={"limit": 100})
    campaigns_list = list(campaigns)

    # Get ad sets
    adsets = account.get_ad_sets(fields=["name", "status", "campaign_id"], params={"limit": 100})
    adsets_list = list(adsets)

    # Get ads
    ads = account.get_ads(fields=["name", "status", "adset_id"], params={"limit": 100})
    ads_list = list(ads)

    overview = {
        "account": account_info,
        "campaigns": {
            "total": len(campaigns_list),
            "active": len([c for c in campaigns_list if c.get("status") == "ACTIVE"]),
            "paused": len([c for c in campaigns_list if c.get("status") == "PAUSED"]),
        },
        "adsets": {
            "total": len(adsets_list),
            "active": len([a for a in adsets_list if a.get("status") == "ACTIVE"]),
            "paused": len([a for a in adsets_list if a.get("status") == "PAUSED"]),
        },
        "ads": {
            "total": len(ads_list),
            "active": len([a for a in ads_list if a.get("status") == "ACTIVE"]),
            "paused": len([a for a in ads_list if a.get("status") == "PAUSED"]),
        },
    }

    if include_insights:
        # Get last 7 days performance
        insights = account.get_insights(
            fields=["impressions", "clicks", "spend", "conversions"],
            params={"date_preset": "last_7d", "level": "account"},
        )
        insights_data = list(insights)
        if insights_data:
            overview["last_7d_performance"] = insights_data[0]

    return overview


@wrapped_fn_tool
def get_active_campaigns_with_performance(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Get all active campaigns with their performance metrics."""
    account = AdAccount(ad_account_id)

    # Get active campaigns with insights
    insights = account.get_insights(
        fields=[
            "campaign_name",
            "campaign_id",
            "impressions",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
        ],
        params={
            "date_preset": date_preset,
            "level": "campaign",
            "filtering": [
                {"field": "campaign.effective_status", "operator": "IN", "value": ["ACTIVE"]},
                {"field": "impressions", "operator": "GREATER_THAN", "value": 0},
            ],
        },
    )

    return list(insights)


@wrapped_fn_tool
def bulk_pause_campaigns(
    ad_account_id: str,
    campaign_ids: list[str],
) -> str:
    """Pause multiple campaigns at once."""
    results = []
    for campaign_id in campaign_ids:
        try:
            from facebook_business.adobjects.campaign import Campaign

            campaign = Campaign(campaign_id)
            result = campaign.api_update(fields=[], params={"status": "PAUSED"})
            results.append({"campaign_id": campaign_id, "status": "success", "result": result})
        except Exception as e:
            results.append({"campaign_id": campaign_id, "status": "error", "error": str(e)})

    return results


@wrapped_fn_tool
def create_saved_audience_from_criteria(
    ad_account_id: str,
    audience_name: str,
    description: str,
    targeting_spec: dict[str, Any],
) -> str:
    """Create a saved audience with specific targeting criteria."""
    account = AdAccount(ad_account_id)

    # Create saved audience
    audience = account.create_saved_audience(
        fields=[],
        params={
            "name": audience_name,
            "description": description,
            "targeting": targeting_spec,
        },
    )

    return audience


@wrapped_fn_tool
def get_targeting_suggestions_for_interests(
    ad_account_id: str,
    interest_keywords: list[str],
) -> str:
    """Get targeting suggestions based on interest keywords."""
    account = AdAccount(ad_account_id)
    all_suggestions = []

    for keyword in interest_keywords:
        suggestions = account.get_targeting_search(
            fields=[],
            params={
                "q": keyword,
                "type": "adinterest",
                "limit": 10,
            },
        )
        all_suggestions.extend(list(suggestions))

    return all_suggestions


@wrapped_fn_tool
def estimate_audience_size(
    ad_account_id: str,
    targeting_spec: dict[str, Any],
) -> str:
    """Estimate the size of an audience based on targeting criteria."""
    account = AdAccount(ad_account_id)

    estimate = account.get_reach_estimate(
        fields=[],
        params={
            "targeting_spec": targeting_spec,
            "optimization_goal": "IMPRESSIONS",
        },
    )

    return list(estimate)


#  ---- Helper tools ----
@wrapped_fn_tool
def list_available_tools_by_category() -> str:
    """List all available tools organized by category for easier discovery."""
    return """
AVAILABLE TOOLS BY CATEGORY:

🚀 QUICK START WORKFLOWS:
- get_account_structure_overview: See complete account hierarchy
- create_complete_campaign: Simple campaign creation
- create_traffic_campaign_workflow: Traffic campaign with targeting
- create_conversion_campaign_workflow: Conversion campaign with pixel
- get_active_campaigns_with_performance: Monitor active campaigns

📊 CAMPAIGN MANAGEMENT:
- get_campaigns: List all campaigns
- create_campaign: Create new campaign
- delete_campaigns: Delete campaigns
- get_campaigns_by_labels: Filter by labels
- bulk_pause_campaigns: Pause multiple campaigns

🎯 AD SET MANAGEMENT:
- get_ad_sets: List all ad sets
- create_ad_set: Create new ad set
- get_ad_sets_by_labels: Filter by labels

📢 AD MANAGEMENT:
- get_ads: List all ads
- create_ad: Create new ad
- get_ads_by_labels: Filter by labels

🎨 CREATIVE MANAGEMENT:
- get_ad_creatives: List creatives
- create_ad_creative: Create creative
- get_ad_images: List images
- create_ad_image: Upload image
- get_ad_videos: List videos
- create_ad_video: Upload video

👥 AUDIENCE MANAGEMENT:
- get_custom_audiences: List custom audiences
- create_custom_audience: Create custom audience
- create_saved_audience_from_criteria: Save targeting as audience
- get_saved_audiences: List saved audiences

🎯 TARGETING TOOLS:
- get_targeting_browse: Browse targeting options
- get_targeting_search: Search targeting options
- get_targeting_suggestions: Get suggestions
- get_targeting_suggestions_for_interests: Interest suggestions
- estimate_audience_size: Estimate reach
- get_reach_estimate: Detailed reach estimate
- get_delivery_estimate: Delivery estimates

📈 INSIGHTS & REPORTING:
- get_insights: Get performance data
- get_insights_async: Async insights for large queries

⚙️ ADVANCED TOOLS:
- get_usage_on_ad_account: See all SDK methods
- run_any_ad_account_fn: Call any SDK method directly
"""


@wrapped_fn_tool
def get_common_field_names() -> str:
    """Get commonly used field names for various objects."""
    return """
COMMON FIELD NAMES BY OBJECT TYPE:

Campaign Fields:
- id, name, status, objective
- daily_budget, lifetime_budget
- start_time, stop_time
- created_time, updated_time
- effective_status
- spend_cap
- buying_type

AdSet Fields:
- id, name, status
- campaign_id
- daily_budget, lifetime_budget
- start_time, end_time
- targeting
- optimization_goal
- billing_event
- bid_strategy
- promoted_object

Ad Fields:
- id, name, status
- adset_id, campaign_id
- creative
- created_time
- effective_status
- recommendations

Insights Fields:
- impressions, reach, frequency
- clicks, unique_clicks, ctr
- spend, cpm, cpc, cpp
- conversions, conversion_values
- purchase_roas
- actions, action_values
- quality_ranking
- engagement_rate_ranking
- conversion_rate_ranking

Targeting Fields:
- geo_locations
- age_min, age_max
- genders
- interests
- behaviors
- custom_audiences
- excluded_custom_audiences
- device_platforms
- publisher_platforms
- facebook_positions
"""


@wrapped_fn_tool
def get_campaign_objective_guide() -> str:
    """Get a guide to choosing the right campaign objective."""
    return """
CAMPAIGN OBJECTIVE GUIDE:

🎯 AWARENESS OBJECTIVES:
- BRAND_AWARENESS: Increase brand recall
- REACH: Show ads to maximum people
- VIDEO_VIEWS: Get more video views

🔗 CONSIDERATION OBJECTIVES:
- TRAFFIC: Send people to website/app
- ENGAGEMENT: Get post engagement
- APP_INSTALLS: Drive app installations
- MESSAGES: Get more messages
- LEAD_GENERATION: Collect leads
- LINK_CLICKS: Optimize for link clicks

💰 CONVERSION OBJECTIVES:
- CONVERSIONS: Drive valuable actions
- PRODUCT_CATALOG_SALES: Dynamic product ads
- STORE_TRAFFIC: Drive foot traffic

RECOMMENDATIONS:
- E-commerce: Use CONVERSIONS or PRODUCT_CATALOG_SALES
- Lead Gen: Use LEAD_GENERATION or CONVERSIONS
- Content/Blog: Use TRAFFIC or LINK_CLICKS
- Brand Building: Use REACH or VIDEO_VIEWS
- App Marketing: Use APP_INSTALLS

NOTE: Objective affects available optimization options and bidding strategies.
"""


#  ---- Labels and Rules ----
@wrapped_fn_tool
def get_ad_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_labels(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_label(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_rules_library(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_rules_library(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_rules_library(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_rules_library(fields=fields, params=params)


#  ---- Instagram and Pages ----
@wrapped_fn_tool
def get_instagram_accounts(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_instagram_accounts(fields=fields, params=params)


@wrapped_fn_tool
def get_connected_instagram_accounts(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_connected_instagram_accounts(fields=fields, params=params)


@wrapped_fn_tool
def get_promote_pages(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_promote_pages(fields=fields, params=params)


#  ---- Applications ----
@wrapped_fn_tool
def get_applications(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_applications(fields=fields, params=params)


@wrapped_fn_tool
def get_advertisable_applications(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_advertisable_applications(fields=fields, params=params)


#  ---- Advanced features ----
@wrapped_fn_tool
def get_saved_audiences(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_saved_audiences(fields=fields, params=params)


@wrapped_fn_tool
def get_custom_conversions(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_custom_conversions(fields=fields, params=params)


@wrapped_fn_tool
def create_custom_conversion(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_custom_conversion(fields=fields, params=params)


@wrapped_fn_tool
def get_activities(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_activities(fields=fields, params=params)


@wrapped_fn_tool
def get_minimum_budgets(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_minimum_budgets(fields=fields, params=params)


@wrapped_fn_tool
def get_broad_targeting_categories(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_broad_targeting_categories(fields=fields, params=params)


# ---- tool docstrings ----

fields_src = inspect.getsource(AdAccount.Field)

# Core API methods
get_ad_account.__doc__ = f"""Gets an AdAccount object by ID.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: {fields_src}

Source code:
{safe_getsource(AdAccount.api_get)}
"""

update_ad_account.__doc__ = f"""Updates an AdAccount object.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: {fields_src}

Source code:
{safe_getsource(AdAccount.api_update)}
"""

# Campaign management
get_campaigns.__doc__ = f"""Get campaigns for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_campaigns)}
"""

create_campaign.__doc__ = f"""Create a new campaign in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Campaign creation parameters

Source code:
{safe_getsource(AdAccount.create_campaign)}
"""

delete_campaigns.__doc__ = f"""Delete campaigns from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Deletion parameters

Source code:
{safe_getsource(AdAccount.delete_campaigns)}
"""

get_campaigns_by_labels.__doc__ = f"""Get campaigns filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_campaigns_by_labels)}
"""

# Ad Set management
get_ad_sets.__doc__ = f"""Get ad sets for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_sets)}
"""

create_ad_set.__doc__ = f"""Create a new ad set in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Ad set creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_set)}
"""

get_ad_sets_by_labels.__doc__ = f"""Get ad sets filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ad_sets_by_labels)}
"""

# Ad management
get_ads.__doc__ = f"""Get ads for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ads)}
"""

create_ad.__doc__ = f"""Create a new ad in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Ad creation parameters

Source code:
{safe_getsource(AdAccount.create_ad)}
"""

get_ads_by_labels.__doc__ = f"""Get ads filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ads_by_labels)}
"""

# Creative management
get_ad_creatives.__doc__ = f"""Get ad creatives for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_creatives)}
"""

create_ad_creative.__doc__ = f"""Create a new ad creative in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Creative creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_creative)}
"""

get_ad_creatives_by_labels.__doc__ = f"""Get ad creatives filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ad_creatives_by_labels)}
"""

# Image management
get_ad_images.__doc__ = f"""Get ad images for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_images)}
"""

create_ad_image.__doc__ = f"""Upload a new ad image to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Image upload parameters

Source code:
{safe_getsource(AdAccount.create_ad_image)}
"""

delete_ad_images.__doc__ = f"""Delete ad images from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Image deletion parameters

Source code:
{safe_getsource(AdAccount.delete_ad_images)}
"""

# Video management
get_ad_videos.__doc__ = f"""Get ad videos for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_videos)}
"""

create_ad_video.__doc__ = f"""Upload a new ad video to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Video upload parameters

Source code:
{safe_getsource(AdAccount.create_ad_video)}
"""

delete_ad_videos.__doc__ = f"""Delete ad videos from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Video deletion parameters

Source code:
{safe_getsource(AdAccount.delete_ad_videos)}
"""

# Custom Audience management
get_custom_audiences.__doc__ = f"""Get custom audiences for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_custom_audiences)}
"""

create_custom_audience.__doc__ = f"""Create a new custom audience in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Custom audience creation parameters

Source code:
{safe_getsource(AdAccount.create_custom_audience)}
"""

# Insights and reporting
get_insights.__doc__ = f"""Get insights for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Insights query parameters
is_async: Whether to run asynchronously

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_insights_async.__doc__ = f"""Get insights asynchronously for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Insights query parameters

Source code:
{safe_getsource(AdAccount.get_insights_async)}
"""

# Targeting tools
get_targeting_browse.__doc__ = f"""Browse targeting options for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Browse parameters

Source code:
{safe_getsource(AdAccount.get_targeting_browse)}
"""

get_targeting_search.__doc__ = f"""Search targeting options for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Search parameters

Source code:
{safe_getsource(AdAccount.get_targeting_search)}
"""

get_targeting_suggestions.__doc__ = f"""Get targeting suggestions for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Suggestion parameters

Source code:
{safe_getsource(AdAccount.get_targeting_suggestions)}
"""

get_reach_estimate.__doc__ = f"""Get reach estimate for targeting.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Targeting parameters

Source code:
{safe_getsource(AdAccount.get_reach_estimate)}
"""

get_delivery_estimate.__doc__ = f"""Get delivery estimate for ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Estimation parameters

Source code:
{safe_getsource(AdAccount.get_delivery_estimate)}
"""

# Pixel management
get_ads_pixels.__doc__ = f"""Get Facebook pixels for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ads_pixels)}
"""

create_ads_pixel.__doc__ = f"""Create a new Facebook pixel for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Pixel creation parameters

Source code:
{safe_getsource(AdAccount.create_ads_pixel)}
"""

# User management
get_users.__doc__ = f"""Get users with access to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_users)}
"""

get_assigned_users.__doc__ = f"""Get assigned users for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_assigned_users)}
"""

create_assigned_user.__doc__ = f"""Assign a user to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: User assignment parameters

Source code:
{safe_getsource(AdAccount.create_assigned_user)}
"""

delete_assigned_users.__doc__ = f"""Remove assigned users from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: User removal parameters

Source code:
{safe_getsource(AdAccount.delete_assigned_users)}
"""

# Labels and Rules
get_ad_labels.__doc__ = f"""Get ad labels for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_labels)}
"""

create_ad_label.__doc__ = f"""Create a new ad label in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Label creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_label)}
"""

get_ad_rules_library.__doc__ = f"""Get ad rules library for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_rules_library)}
"""

create_ad_rules_library.__doc__ = f"""Create new ad rules in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Rule creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_rules_library)}
"""

# Instagram and Pages
get_instagram_accounts.__doc__ = f"""Get Instagram accounts connected to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_instagram_accounts)}
"""

get_connected_instagram_accounts.__doc__ = f"""Get connected Instagram accounts for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_connected_instagram_accounts)}
"""

get_promote_pages.__doc__ = f"""Get pages that can be promoted by this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_promote_pages)}
"""

# Applications
get_applications.__doc__ = f"""Get applications associated with this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_applications)}
"""

get_advertisable_applications.__doc__ = f"""Get advertisable applications for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_advertisable_applications)}
"""

# Advanced features
get_saved_audiences.__doc__ = f"""Get saved audiences for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_saved_audiences)}
"""

get_custom_conversions.__doc__ = f"""Get custom conversions for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_custom_conversions)}
"""

create_custom_conversion.__doc__ = f"""Create a new custom conversion for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Custom conversion creation parameters

Source code:
{safe_getsource(AdAccount.create_custom_conversion)}
"""

get_activities.__doc__ = f"""Get activities for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_activities)}
"""

get_minimum_budgets.__doc__ = f"""Get minimum budget requirements for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_minimum_budgets)}
"""

get_broad_targeting_categories.__doc__ = f"""Get broad targeting categories for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_broad_targeting_categories)}
"""

# Higher-level workflow tools docstrings
create_complete_campaign.__doc__ = f"""Create a complete campaign with common settings in one call.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
campaign_name: Name for the campaign
objective: Campaign objective (e.g., 'LINK_CLICKS', 'CONVERSIONS', 'REACH')
daily_budget: Daily budget in dollars (will be converted to cents)
special_ad_categories: Special ad categories if applicable (e.g., ['CREDIT', 'HOUSING'])

Creates a paused campaign ready for ad sets. Common objectives:
- LINK_CLICKS: Drive traffic to website
- CONVERSIONS: Optimize for conversions
- REACH: Maximize reach
- VIDEO_VIEWS: Video view campaigns
- LEAD_GENERATION: Collect leads

Source code:
{safe_getsource(AdAccount.create_campaign)}
"""

create_traffic_campaign_workflow.__doc__ = """Complete workflow to create a traffic campaign with ad set and targeting.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
campaign_name: Name for the campaign
daily_budget: Daily budget in dollars
destination_url: URL where traffic should be sent
audience_targeting: Additional targeting criteria (merged with defaults)

Creates a complete traffic campaign structure:
1. Campaign with LINK_CLICKS objective
2. Ad set with targeting and budget
3. Returns IDs for creating ads

Default targeting: US, ages 18-65. Override with audience_targeting param.
"""

create_conversion_campaign_workflow.__doc__ = """Complete workflow to create a conversion-optimized campaign.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
campaign_name: Name for the campaign
daily_budget: Daily budget in dollars
pixel_id: Facebook Pixel ID for conversion tracking
conversion_event: Conversion event to optimize for (default: 'Purchase')
audience_targeting: Additional targeting criteria

Creates conversion campaign optimized for specific events:
- Purchase
- AddToCart
- InitiateCheckout
- Lead
- CompleteRegistration

Requires Facebook Pixel to be installed on website.
"""

get_account_structure_overview.__doc__ = """Get a complete overview of account structure with counts and status.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
include_insights: Include last 7 days performance metrics

Returns hierarchical overview:
- Account info (name, status, currency)
- Campaign counts (total, active, paused)
- Ad set counts
- Ad counts
- Optional: Recent performance metrics

Perfect for understanding account structure at a glance.
"""

get_active_campaigns_with_performance.__doc__ = """Get all active campaigns with their performance metrics.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for metrics (default: 'last_7d')

Returns active campaigns with:
- Traffic metrics (impressions, clicks, CTR)
- Cost metrics (spend, CPM, CPC)
- Conversion metrics (conversions, ROAS)

Useful for monitoring and optimization decisions.
"""

bulk_pause_campaigns.__doc__ = """Pause multiple campaigns at once.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
campaign_ids: List of campaign IDs to pause

Batch operation to pause campaigns. Returns success/error status for each.
Useful for budget management or pausing underperforming campaigns.
"""

create_saved_audience_from_criteria.__doc__ = """Create a saved audience with specific targeting criteria.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
audience_name: Name for the saved audience
description: Description of the audience
targeting_spec: Complete targeting specification

Example targeting_spec:
{
  'geo_locations': {'countries': ['US']},
  'age_min': 25,
  'age_max': 45,
  'genders': [1],  # 1=male, 2=female
  'interests': [{'id': '6003139266461', 'name': 'Movies'}],
  'behaviors': [{'id': '6002714895372', 'name': 'Frequent Travelers'}]
}
"""

get_targeting_suggestions_for_interests.__doc__ = """Get targeting suggestions based on interest keywords.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
interest_keywords: List of keywords to search for interests

Finds targetable interests matching keywords.
Returns interest IDs and names for use in targeting.

Example: ['fitness', 'yoga'] returns related targetable interests.
"""

estimate_audience_size.__doc__ = """Estimate the size of an audience based on targeting criteria.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
targeting_spec: Targeting criteria to estimate

Returns estimated daily and monthly reach.
Helps ensure audience isn't too broad or narrow.

Recommended audience sizes:
- Too narrow: < 1,000 daily reach
- Good: 10,000 - 500,000 daily reach
- Too broad: > 5,000,000 daily reach
"""

list_available_tools_by_category.__doc__ = """List all available tools organized by category for easier discovery.

Provides a categorized overview of all tools:
- Quick Start Workflows
- Campaign Management
- Ad Set Management
- Ad Management
- Creative Management
- Audience Management
- Targeting Tools
- Insights & Reporting
- Advanced Tools

Use this to quickly find the right tool for your task.
"""

get_common_field_names.__doc__ = """Get commonly used field names for various objects.

Provides field names for:
- Campaign fields
- AdSet fields
- Ad fields
- Insights fields
- Targeting fields

Essential reference when using get_* or create_* methods.
"""

get_campaign_objective_guide.__doc__ = """Get a guide to choosing the right campaign objective.

Explains all available objectives:
- Awareness objectives
- Consideration objectives
- Conversion objectives

Includes recommendations for different business goals.
"""

# ---- register tools ----
# Helper tools (register first for discoverability)
ad_account_server.tool(list_available_tools_by_category)
ad_account_server.tool(get_common_field_names)
ad_account_server.tool(get_campaign_objective_guide)

# Core tools
ad_account_server.tool(get_usage_on_ad_account)
ad_account_server.tool(run_any_ad_account_fn)

# Higher-level workflow tools
ad_account_server.tool(get_account_structure_overview)
ad_account_server.tool(create_complete_campaign)
ad_account_server.tool(create_traffic_campaign_workflow)
ad_account_server.tool(create_conversion_campaign_workflow)
ad_account_server.tool(get_active_campaigns_with_performance)
ad_account_server.tool(bulk_pause_campaigns)
ad_account_server.tool(create_saved_audience_from_criteria)
ad_account_server.tool(get_targeting_suggestions_for_interests)
ad_account_server.tool(estimate_audience_size)

# Core API methods
ad_account_server.tool(get_ad_account)
ad_account_server.tool(update_ad_account)

# Campaign management
ad_account_server.tool(get_campaigns)
ad_account_server.tool(create_campaign)
ad_account_server.tool(delete_campaigns)
ad_account_server.tool(get_campaigns_by_labels)

# Ad Set management
ad_account_server.tool(get_ad_sets)
ad_account_server.tool(create_ad_set)
ad_account_server.tool(get_ad_sets_by_labels)

# Ad management
ad_account_server.tool(get_ads)
ad_account_server.tool(create_ad)
ad_account_server.tool(get_ads_by_labels)

# Creative management
ad_account_server.tool(get_ad_creatives)
ad_account_server.tool(create_ad_creative)
ad_account_server.tool(get_ad_creatives_by_labels)

# Image management
ad_account_server.tool(get_ad_images)
ad_account_server.tool(create_ad_image)
ad_account_server.tool(delete_ad_images)

# Video management
ad_account_server.tool(get_ad_videos)
ad_account_server.tool(create_ad_video)
ad_account_server.tool(delete_ad_videos)

# Custom Audience management
ad_account_server.tool(get_custom_audiences)
ad_account_server.tool(create_custom_audience)

# Insights and reporting
ad_account_server.tool(get_insights)
ad_account_server.tool(get_insights_async)

# Targeting tools
ad_account_server.tool(get_targeting_browse)
ad_account_server.tool(get_targeting_search)
ad_account_server.tool(get_targeting_suggestions)
ad_account_server.tool(get_reach_estimate)
ad_account_server.tool(get_delivery_estimate)

# Pixel management
ad_account_server.tool(get_ads_pixels)
ad_account_server.tool(create_ads_pixel)

# User management
ad_account_server.tool(get_users)
ad_account_server.tool(get_assigned_users)
ad_account_server.tool(create_assigned_user)
ad_account_server.tool(delete_assigned_users)

# Labels and Rules
ad_account_server.tool(get_ad_labels)
ad_account_server.tool(create_ad_label)
ad_account_server.tool(get_ad_rules_library)
ad_account_server.tool(create_ad_rules_library)

# Instagram and Pages
ad_account_server.tool(get_instagram_accounts)
ad_account_server.tool(get_connected_instagram_accounts)
ad_account_server.tool(get_promote_pages)

# Applications
ad_account_server.tool(get_applications)
ad_account_server.tool(get_advertisable_applications)

# Advanced features
ad_account_server.tool(get_saved_audiences)
ad_account_server.tool(get_custom_conversions)
ad_account_server.tool(create_custom_conversion)
ad_account_server.tool(get_activities)
ad_account_server.tool(get_minimum_budgets)
ad_account_server.tool(get_broad_targeting_categories)
