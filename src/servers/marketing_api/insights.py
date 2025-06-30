"""Insights MCP Server using Facebook Business SDK."""

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
