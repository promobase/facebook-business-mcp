"""Insights MCP Server using Facebook Business SDK."""

from typing import Any

from facebook_business.adobjects.adsinsights import AdsInsights
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)

#  ---- constants ----
server_name = "FacebookInsights"
instructions = """
This is the Insights MCP Server for retrieving Facebook Ads performance data.
always use the `get_usage_on_insights` tool first to understand how to use the methods and fields available.
AdsInsights is not instantiated directly - it's returned from get_insights() calls on AdAccount, Campaign, AdSet, or Ad objects.
"""

insights_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


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


# ---- register tools ----
insights_server.tool(get_usage_on_insights)