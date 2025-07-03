"""Insights MCP Server configuration."""

from fastmcp import FastMCP

# Import all insights operations
from .operations import (
    account_get_insights,
    account_get_insights_async,
    ad_get_insights,
    ad_get_insights_async,
    adset_get_insights,
    adset_get_insights_async,
    campaign_get_insights,
    campaign_get_insights_async,
    get_insights,
    get_insights_async,
)
from .specialized import (
    adset_get_ad_studies,
    adset_get_delivery_estimate,
    adset_get_message_delivery_estimate,
    campaign_get_ad_studies,
)

server_name = "FacebookInsights"
instructions = """
Insights MCP Server for Facebook Business API.

Provides unified insights operations for all levels:
- AdAccount insights
- Campaign insights
- AdSet insights and delivery estimates
- Ad insights
- Ad studies and specialized analytics

Use the generic get_insights() with level parameter or specific functions for each level.
"""

# Initialize server
server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register generic insights tools
server.tool(get_insights)
server.tool(get_insights_async)

# Register level-specific insights tools
server.tool(account_get_insights)
server.tool(account_get_insights_async)
server.tool(campaign_get_insights)
server.tool(campaign_get_insights_async)
server.tool(adset_get_insights)
server.tool(adset_get_insights_async)
server.tool(ad_get_insights)
server.tool(ad_get_insights_async)

# Register specialized insights tools
server.tool(adset_get_delivery_estimate)
server.tool(adset_get_message_delivery_estimate)
server.tool(campaign_get_ad_studies)
server.tool(adset_get_ad_studies)
