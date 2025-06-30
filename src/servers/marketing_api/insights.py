"""Insights MCP Server using Facebook Business SDK."""

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookInsights"
instructions = """
This is the Insights MCP Server for retrieving Facebook Ads performance data.

IMPORTANT: AdsInsights is not instantiated directly - it's returned from get_insights() calls on AdAccount, Campaign, AdSet, or Ad objects.
Use the parent object's get_insights() method to retrieve insights data.

The tools here help you understand the available fields and parameters for insights queries.
"""

insights_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Helper tools for insights ----
@wrapped_fn_tool
def get_insights_fields() -> str:
    fields = AdsInsights._field_types
    return f"Available AdsInsights fields:\n{fields}"


@wrapped_fn_tool
def get_insights_enums() -> str:
    enums = AdsInsights._get_field_enum_info()
    return f"Available AdsInsights enums:\n{enums}"


@wrapped_fn_tool
def get_insights_breakdowns() -> str:
    breakdowns = AdsInsights.Breakdowns._values
    return f"Available AdsInsights breakdowns:\n{breakdowns}"


@wrapped_fn_tool
def get_insights_date_presets() -> str:
    date_presets = AdsInsights.DatePreset._values
    return f"Available AdsInsights date presets:\n{date_presets}"


@wrapped_fn_tool
def get_insights_levels() -> str:
    levels = AdsInsights.Level._values
    return f"Available AdsInsights levels:\n{levels}"


@wrapped_fn_tool
def get_insights_action_breakdowns() -> str:
    action_breakdowns = AdsInsights.ActionBreakdowns._values
    return f"Available AdsInsights action breakdowns:\n{action_breakdowns}"


@wrapped_fn_tool
def get_insights_action_report_time() -> str:
    action_report_time = AdsInsights.ActionReportTime._values
    return f"Available AdsInsights action report time:\n{action_report_time}"


@wrapped_fn_tool
def analyze_roas_by_campaign(
    ad_account_id: str,
    date_preset: str = "last_7d",
    min_spend: float = 10.0,
) -> str:
    """Analyze Return on Ad Spend (ROAS) by campaign with revenue breakdown."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "campaign_name",
            "campaign_id",
            "spend",
            "purchase_roas",
            "website_purchase_roas",
            "actions",
            "action_values",
            "conversions",
            "conversion_values",
            "cost_per_action_type",
            "return_on_ad_spend",
        ],
        params={
            "date_preset": date_preset,
            "level": "campaign",
            "filtering": [{"field": "spend", "operator": "GREATER_THAN", "value": min_spend}],
            "action_attribution_windows": ["7d_click", "1d_view"],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_geographic_performance(
    ad_account_id: str,
    date_preset: str = "last_7d",
    breakdown_level: str = "country",
) -> str:
    """Analyze performance by geographic location."""
    # Validate breakdown level
    valid_levels = ["country", "region", "city", "zip"]
    if breakdown_level not in valid_levels:
        breakdown_level = "country"

    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "impressions",
            "reach",
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
            "level": "account",
            "breakdowns": [breakdown_level],
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 100}],
            "sort": ["spend_descending"],
            "limit": 50,
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_device_performance_analysis(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze performance by device type and platform."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "impressions",
            "reach",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
            "mobile_app_install",
            "website_clicks",
        ],
        params={
            "date_preset": date_preset,
            "level": "account",
            "breakdowns": ["device_platform", "impression_device"],
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 100}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_hourly_performance_patterns(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze performance patterns by hour of day."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "hourly_stats_aggregated_by_advertiser_time_zone",
            "impressions",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
        ],
        params={
            "date_preset": date_preset,
            "level": "account",
            "breakdowns": ["hourly_stats_aggregated_by_advertiser_time_zone"],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_custom_audience_performance(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze performance of custom audiences vs broad targeting."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "adset_name",
            "campaign_name",
            "impressions",
            "reach",
            "frequency",
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
            "level": "adset",
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 1000}],
            "sort": ["purchase_roas_descending"],
            "limit": 100,
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_common_insights_params() -> str:
    return """Common parameters for get_insights() calls:

Required:
- fields: List of metric fields to retrieve (e.g., ['impressions', 'clicks', 'spend'])

Optional:
- params: Dictionary with query parameters:
  - date_preset: Predefined date range (e.g., 'last_7d', 'last_30d')
  - time_range: Custom date range {'since': 'YYYY-MM-DD', 'until': 'YYYY-MM-DD'}
  - level: Aggregation level ('account', 'campaign', 'adset', 'ad')
  - breakdowns: List of dimensions to break down by (e.g., ['age', 'gender'])
  - filtering: List of filters to apply
  - action_breakdowns: List of action breakdowns
  - time_increment: Time granularity (1-90 for daily, 'monthly', 'all_days')
  - use_account_attribution_setting: Use account's attribution setting
  - limit: Number of results to return

Example:
account.get_insights(
    fields=['impressions', 'clicks', 'spend', 'cpm', 'cpc', 'ctr'],
    params={
        'date_preset': 'last_7d',
        'level': 'ad',
        'breakdowns': ['age', 'gender']
    }
)"""


@wrapped_fn_tool
def get_insights_filtering_examples() -> str:
    return """Examples of filtering in get_insights() calls:

Filtering allows you to include/exclude specific data from insights results.

Format: List of dictionaries with 'field', 'operator', and 'value'

Example filters:
[
    # Only iOS devices
    {'field': 'publisher_platform', 'operator': 'IN', 'value': ['facebook']},
    
    # Only active campaigns
    {'field': 'campaign.effective_status', 'operator': 'IN', 'value': ['ACTIVE']},
    
    # Impressions greater than 1000
    {'field': 'impressions', 'operator': 'GREATER_THAN', 'value': 1000},
    
    # Specific age ranges
    {'field': 'age', 'operator': 'IN', 'value': ['25-34', '35-44']}
]

Common operators: IN, NOT_IN, EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN, CONTAIN, NOT_CONTAIN"""


@wrapped_fn_tool
def get_insights_metrics_descriptions() -> str:
    return """Common AdsInsights metrics and their descriptions:

Traffic Metrics:
- impressions: Number of times ads were shown
- reach: Number of unique people who saw ads
- frequency: Average number of times each person saw ads
- clicks: Total clicks on ads (all types)
- unique_clicks: Number of unique people who clicked

Cost Metrics:
- spend: Total amount spent
- cpm: Cost per 1000 impressions
- cpc: Cost per click
- cpp: Cost per purchase
- ctr: Click-through rate (clicks/impressions)

Conversion Metrics:
- conversions: Total conversions
- conversion_rate_ranking: How your conversion rate compares
- cost_per_conversion: Average cost for each conversion
- purchase_roas: Return on ad spend from purchases

Engagement Metrics:
- engagement_rate_ranking: How your engagement rate compares
- post_engagement: Total post engagements
- page_engagement: Total page engagements
- video_play_actions: Video plays
- video_avg_time_watched_actions: Average video watch time

Quality Metrics:
- quality_ranking: How your ad quality compares
- auction_competitiveness: Your competitiveness in auction
- auction_max_competitor_bid: Highest competing bid"""


@wrapped_fn_tool
def get_insights_export_methods() -> str:
    return """Methods for exporting and processing AdsInsights data:

Basic Export:
# Get insights as a cursor
insights = account.get_insights(fields=[...], params={...})

# Convert to list
insights_list = list(insights)

# Export single insight
if insights_list:
    data = insights_list[0].export_all_data()  # Returns dict

# Export all insights
all_data = [insight.export_all_data() for insight in insights_list]

Advanced Processing:
# Access specific fields
for insight in insights:
    print(f"Spend: {insight['spend']}")
    print(f"Impressions: {insight['impressions']}")
    print(f"CTR: {insight['ctr']}")

# Filter insights
high_spend = [i for i in insights_list if float(i.get('spend', 0)) > 100]

# Aggregate data
total_spend = sum(float(i.get('spend', 0)) for i in insights_list)

Async Export for Large Datasets:
report = account.get_insights_async(fields=[...], params={...})
# Wait for completion
time.sleep(5)
status = report.api_get()
if status['async_status'] == 'Job Completed':
    results = report.get_result()
    insights_data = list(results)"""


@wrapped_fn_tool
def get_insights_time_increment_options() -> str:
    return """Time increment options for AdsInsights queries:

time_increment parameter controls data granularity over time:

1. Daily breakdowns:
   - Use integer 1-90 for N-day windows
   - Example: time_increment=1 (daily), time_increment=7 (weekly)

2. Fixed periods:
   - 'monthly': Monthly breakdowns
   - 'all_days': Single row for entire period

Examples:
# Daily data for last 7 days
params = {
    'date_preset': 'last_7d',
    'time_increment': 1
}

# Weekly data for last month  
params = {
    'date_preset': 'last_30d',
    'time_increment': 7
}

# Monthly data for last quarter
params = {
    'date_preset': 'last_90d',
    'time_increment': 'monthly'
}

# Single total for date range
params = {
    'time_range': {'since': '2024-01-01', 'until': '2024-12-31'},
    'time_increment': 'all_days'
}

Note: time_increment affects the number of rows returned and API rate limits."""


@wrapped_fn_tool
def get_insights_attribution_windows() -> str:
    return """Attribution window options for AdsInsights queries:

Attribution windows determine how conversions are credited to ads:

Default windows (account setting):
params = {
    'use_account_attribution_setting': True
}

Custom attribution windows:
params = {
    'action_attribution_windows': [
        'actions:1d_click',      # 1-day click
        'actions:7d_click',      # 7-day click  
        'actions:28d_click',     # 28-day click
        'actions:1d_view',       # 1-day view
        'actions:7d_view',       # 7-day view
        'actions:28d_view'       # 28-day view
    ]
}

Specific conversion windows:
params = {
    'action_attribution_windows': [
        'purchase:1d_click',
        'purchase:1d_view',
        'add_to_cart:1d_click',
        'lead:7d_click'
    ]
}

Comparing attribution models:
params = {
    'action_attribution_windows': [
        'actions:1d_click',
        'actions:7d_click',
        'actions:28d_click'
    ],
    'fields': [
        'actions',
        'action_values',
        'cost_per_action_type'
    ]
}

Note: Attribution windows significantly impact reported conversions and ROAS."""


#  ---- Higher-level analysis tools ----
@wrapped_fn_tool
def get_account_performance_summary(
    ad_account_id: str,
    date_preset: str = "last_7d",
    level: str = "account",
) -> str:
    """Get high-level performance summary for an ad account."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "impressions",
            "reach",
            "frequency",
            "clicks",
            "unique_clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
            "actions",
            "action_values",
            "cost_per_action_type",
        ],
        params={
            "date_preset": date_preset,
            "level": level,
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_campaign_performance_comparison(
    ad_account_id: str,
    date_preset: str = "last_7d",
    fields: list[str] = [],
) -> str:
    """Compare performance across all campaigns in an account."""
    if not fields:
        fields = [
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
        ]

    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=fields,
        params={
            "date_preset": date_preset,
            "level": "campaign",
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 0}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_ad_performance_by_creative(
    ad_account_id: str,
    date_preset: str = "last_7d",
    limit: int = 50,
) -> str:
    """Analyze ad performance grouped by creative elements."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "ad_name",
            "ad_id",
            "adset_name",
            "campaign_name",
            "impressions",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
            "frequency",
            "quality_ranking",
            "engagement_rate_ranking",
            "conversion_rate_ranking",
        ],
        params={
            "date_preset": date_preset,
            "level": "ad",
            "limit": limit,
            "sort": ["spend_descending"],
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 100}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_audience_breakdown_analysis(
    ad_account_id: str,
    breakdowns: list[str] = [],
    date_preset: str = "last_7d",
    level: str = "account",
) -> str:
    """Analyze performance broken down by audience segments."""
    if not breakdowns:
        breakdowns = ["age", "gender"]

    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "impressions",
            "reach",
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
            "level": level,
            "breakdowns": breakdowns,
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 100}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_placement_performance_analysis(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze performance by placement (Facebook, Instagram, Audience Network, etc)."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "impressions",
            "reach",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
            "frequency",
        ],
        params={
            "date_preset": date_preset,
            "level": "account",
            "breakdowns": ["publisher_platform", "platform_position"],
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 100}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_time_series_performance(
    ad_account_id: str,
    date_preset: str = "last_30d",
    time_increment: int = 1,
    level: str = "account",
) -> str:
    """Get daily/weekly performance trends over time."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "date_start",
            "date_stop",
            "impressions",
            "reach",
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
            "level": level,
            "time_increment": time_increment,
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_video_performance_metrics(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Get detailed video performance metrics for video ads."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "campaign_name",
            "adset_name",
            "ad_name",
            "impressions",
            "spend",
            "video_play_actions",
            "video_p25_watched_actions",
            "video_p50_watched_actions",
            "video_p75_watched_actions",
            "video_p95_watched_actions",
            "video_p100_watched_actions",
            "video_avg_time_watched_actions",
            "cost_per_thruplay",
            "video_thruplay_watched_actions",
        ],
        params={
            "date_preset": date_preset,
            "level": "ad",
            "filtering": [{"field": "video_play_actions", "operator": "GREATER_THAN", "value": 0}],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_conversion_funnel_analysis(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze conversion funnel from impressions to purchases."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "campaign_name",
            "impressions",
            "reach",
            "clicks",
            "unique_clicks",
            "landing_page_views",
            "link_clicks",
            "add_to_cart",
            "initiated_checkout",
            "purchase",
            "omni_purchase",
            "spend",
            "purchase_roas",
            "website_purchase_roas",
            "actions",
            "action_values",
            "cost_per_action_type",
        ],
        params={
            "date_preset": date_preset,
            "level": "campaign",
            "action_attribution_windows": ["7d_click", "1d_view"],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_mobile_app_performance(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Get mobile app install and engagement metrics."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "campaign_name",
            "adset_name",
            "impressions",
            "clicks",
            "spend",
            "mobile_app_install",
            "app_installs",
            "cost_per_mobile_app_install",
            "cost_per_app_install",
            "app_use",
            "app_custom_event",
            "actions",
            "action_values",
            "cost_per_action_type",
        ],
        params={
            "date_preset": date_preset,
            "level": "adset",
            "filtering": [
                {"field": "objective", "operator": "IN", "value": ["APP_INSTALLS", "LINK_CLICKS"]}
            ],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


@wrapped_fn_tool
def get_quality_ranking_analysis(
    ad_account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze ad quality rankings and competitive metrics."""
    account = AdAccount(ad_account_id)
    insights = account.get_insights(
        fields=[
            "ad_name",
            "adset_name",
            "campaign_name",
            "impressions",
            "spend",
            "quality_ranking",
            "engagement_rate_ranking",
            "conversion_rate_ranking",
            "auction_bid",
            "auction_competitiveness",
            "auction_max_competitor_bid",
            "cpm",
            "cpc",
            "ctr",
        ],
        params={
            "date_preset": date_preset,
            "level": "ad",
            "filtering": [{"field": "impressions", "operator": "GREATER_THAN", "value": 1000}],
            "sort": ["quality_ranking_ascending"],
            "use_account_attribution_setting": True,
        },
    )
    return list(insights)


#  ---- Dynamic tools ----
@log_execution
@handle_facebook_errors
def get_usage_on_insights(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use insights and available fields. This includes examples.
    Optionally, you can pass in a method/field name and you will see the src code for it.
    """
    field_enum_info: dict = AdsInsights._get_field_enum_info()
    methods = list_callable_methods(AdsInsights)

    usage = f"""
    This is the AdsInsights wrapper on Facebook Business Python SDK. 
    AdsInsights objects are returned from get_insights() calls on AdAccount, Campaign, AdSet, or Ad objects.
    
    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {AdsInsights._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    # Get insights from different levels
    account = AdAccount('act_123')
    insights = account.get_insights(
        fields=['impressions', 'clicks', 'spend', 'cpm', 'cpc', 'ctr'],
        params={{
            'date_preset': 'last_7d',
            'level': 'ad',
            'breakdowns': ['age', 'gender']
        }}
    )
    
    campaign = Campaign('123')
    insights = campaign.get_insights(fields=[..], params=..)
    
    # Common fields: impressions, clicks, spend, reach, frequency, cpm, cpc, ctr
    # Common params: date_preset, time_range, level, breakdowns, filtering
    
    # Async insights for large queries
    report = account.get_insights_async(fields=[..], params=..)
    # Check status: report.api_get()['async_status']
    # Get results when ready: report.get_result()
    
    # Export insights
    insights_list = list(insights)  # Convert cursor to list
    # insights_list[0].export_all_data()  # Export as dict
    """

    if fn:
        # append method/field src
        if hasattr(AdsInsights, fn):
            attr = getattr(AdsInsights, fn)
            if callable(attr):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(attr)}"
            else:
                usage += f"\n\nHere is the definition for {fn}:\n{safe_getsource(attr)}"
        else:
            usage += f"\n\nAdsInsights does not have attribute '{fn}'."
    return usage


# ---- tool docstrings ----

# Higher-level analysis tools docstrings
get_account_performance_summary.__doc__ = f"""Get high-level performance summary for an ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)
level: Aggregation level (default: account)

Returns comprehensive metrics including traffic, cost, and conversion data.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_campaign_performance_comparison.__doc__ = f"""Compare performance across all campaigns in an account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)
fields: Custom fields to retrieve (optional)

Useful for identifying top and bottom performing campaigns.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_ad_performance_by_creative.__doc__ = f"""Analyze ad performance grouped by creative elements.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)
limit: Maximum number of ads to return (default: 50)

Returns top spending ads with quality rankings and performance metrics.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_audience_breakdown_analysis.__doc__ = f"""Analyze performance broken down by audience segments.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
breakdowns: List of breakdown dimensions (default: ['age', 'gender'])
date_preset: Time period for the report (default: last_7d)
level: Aggregation level (default: account)

Essential for understanding which audiences perform best.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_placement_performance_analysis.__doc__ = f"""Analyze performance by placement (Facebook, Instagram, Audience Network, etc).
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Helps optimize budget allocation across placements.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_time_series_performance.__doc__ = f"""Get daily/weekly performance trends over time.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_30d)
time_increment: Time granularity in days (default: 1 for daily)
level: Aggregation level (default: account)

Perfect for trend analysis and identifying patterns.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_video_performance_metrics.__doc__ = f"""Get detailed video performance metrics for video ads.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Includes video completion rates and engagement metrics.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_conversion_funnel_analysis.__doc__ = f"""Analyze conversion funnel from impressions to purchases.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Shows full funnel metrics with attribution windows.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_mobile_app_performance.__doc__ = f"""Get mobile app install and engagement metrics.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Specialized metrics for app install campaigns.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_quality_ranking_analysis.__doc__ = f"""Analyze ad quality rankings and competitive metrics.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Identifies ads with quality issues affecting performance.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

# Helper method docstrings
get_insights_fields.__doc__ = f"""Get all available fields for AdsInsights queries.

This shows all possible fields you can request in a get_insights() call.
Common fields include impressions, clicks, spend, reach, frequency, cpm, cpc, ctr.

AdsInsights Field class source:
{safe_getsource(AdsInsights.Field)}
"""

get_insights_enums.__doc__ = f"""Get all available enums for AdsInsights queries.

This shows all enum values that can be used in insights parameters.
Includes breakdowns, date presets, levels, and more.

Source for getting enum info:
{safe_getsource(AdsInsights._get_field_enum_info)}
"""

get_insights_breakdowns.__doc__ = f"""Get available breakdown options for AdsInsights queries.

Breakdowns allow you to segment your insights data by various dimensions.
Common breakdowns include age, gender, country, placement, device_platform.

AdsInsights Breakdowns class source:
{safe_getsource(AdsInsights.Breakdowns)}
"""

get_insights_date_presets.__doc__ = f"""Get available date preset options for AdsInsights queries.

Date presets provide convenient time ranges for insights queries.
Common presets include today, yesterday, last_7d, last_30d, this_month, lifetime.

AdsInsights DatePreset class source:
{safe_getsource(AdsInsights.DatePreset)}
"""

get_insights_levels.__doc__ = f"""Get available aggregation levels for AdsInsights queries.

Levels determine the granularity of insights data.
Available levels: account, campaign, adset, ad.

AdsInsights Level class source:
{safe_getsource(AdsInsights.Level)}
"""

get_insights_action_breakdowns.__doc__ = f"""Get available action breakdown options for AdsInsights queries.

Action breakdowns provide detailed attribution windows for conversions.
Common options include action_type, action_target_id, action_destination.

AdsInsights ActionBreakdowns class source:
{safe_getsource(AdsInsights.ActionBreakdowns)}
"""

get_insights_action_report_time.__doc__ = f"""Get available action report time options for AdsInsights queries.

Determines whether actions are reported based on impression or conversion time.
Options: impression, conversion.

AdsInsights ActionReportTime class source:
{safe_getsource(AdsInsights.ActionReportTime)}
"""

analyze_roas_by_campaign.__doc__ = f"""Analyze Return on Ad Spend (ROAS) by campaign with revenue breakdown.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)
min_spend: Minimum spend threshold to include campaigns (default: 10.0)

Focuses on revenue generation and profitability metrics.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_geographic_performance.__doc__ = f"""Analyze performance by geographic location.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)
breakdown_level: Geographic granularity - 'country', 'region', 'city', or 'zip' (default: country)

Helps identify best performing geographic markets.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_device_performance_analysis.__doc__ = f"""Analyze performance by device type and platform.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Shows performance differences between mobile, desktop, and tablet.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_hourly_performance_patterns.__doc__ = f"""Analyze performance patterns by hour of day.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Identifies optimal times for ad delivery.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_custom_audience_performance.__doc__ = f"""Analyze performance of custom audiences vs broad targeting.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
date_preset: Time period for the report (default: last_7d)

Compares effectiveness of different audience strategies.

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_common_insights_params.__doc__ = """Get common parameters used in get_insights() calls.

Provides a comprehensive guide to all parameters available for insights queries.
Includes required fields, optional parameters, and usage examples.

This is essential for understanding how to structure get_insights() calls.
"""

get_insights_filtering_examples.__doc__ = """Get examples of filtering in get_insights() calls.

Filtering is crucial for narrowing down insights to specific segments.
Shows format, operators, and practical examples of common filters.

Useful for targeting specific platforms, statuses, metrics thresholds, or demographics.
"""

get_insights_metrics_descriptions.__doc__ = """Get descriptions of common AdsInsights metrics.

Provides detailed explanations of what each metric means and measures.
Organized by category: Traffic, Cost, Conversion, Engagement, and Quality.

Essential reference for understanding which fields to request in insights queries.
"""

get_insights_export_methods.__doc__ = """Get methods for exporting and processing AdsInsights data.

Shows how to convert insights cursors to usable data formats.
Includes examples for basic export, advanced processing, and async operations.

Useful for handling insights results and integrating with data pipelines.
"""

get_insights_time_increment_options.__doc__ = """Get time increment options for AdsInsights queries.

Explains how to control temporal granularity of insights data.
Shows daily, weekly, monthly, and custom period options.

Critical for time-series analysis and controlling data volume.
"""

get_insights_attribution_windows.__doc__ = """Get attribution window options for AdsInsights queries.

Explains how to configure conversion attribution windows.
Shows default settings, custom windows, and comparison strategies.

Essential for accurate conversion tracking and ROAS measurement.
"""

# ---- register tools ----
# Core tools
insights_server.tool(get_usage_on_insights)

# Higher-level analysis tools
insights_server.tool(get_account_performance_summary)
insights_server.tool(get_campaign_performance_comparison)
insights_server.tool(get_ad_performance_by_creative)
insights_server.tool(get_audience_breakdown_analysis)
insights_server.tool(get_placement_performance_analysis)
insights_server.tool(get_time_series_performance)
insights_server.tool(get_video_performance_metrics)
insights_server.tool(get_conversion_funnel_analysis)
insights_server.tool(get_mobile_app_performance)
insights_server.tool(get_quality_ranking_analysis)
insights_server.tool(analyze_roas_by_campaign)
insights_server.tool(get_geographic_performance)
insights_server.tool(get_device_performance_analysis)
insights_server.tool(get_hourly_performance_patterns)
insights_server.tool(get_custom_audience_performance)

# Helper tools
insights_server.tool(get_insights_fields)
insights_server.tool(get_insights_enums)
insights_server.tool(get_insights_breakdowns)
insights_server.tool(get_insights_date_presets)
insights_server.tool(get_insights_levels)
insights_server.tool(get_insights_action_breakdowns)
insights_server.tool(get_insights_action_report_time)
insights_server.tool(get_common_insights_params)
insights_server.tool(get_insights_filtering_examples)
insights_server.tool(get_insights_metrics_descriptions)
insights_server.tool(get_insights_export_methods)
insights_server.tool(get_insights_time_increment_options)
insights_server.tool(get_insights_attribution_windows)
