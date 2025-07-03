"""Campaign MCP Server configuration."""

from fastmcp import FastMCP

from .ad_sets import (
    campaign_create_budget_schedule,
    campaign_get_ad_sets,
)
from .ads import (
    campaign_create_ad_label,
    campaign_get_ad_rules_governed,
    campaign_get_ads,
)
from .copies import (
    campaign_create_copy,
    campaign_get_copies,
)

# Import all campaign operations
from .crud import (
    adaccount_delete_campaigns,
    adaccount_get_campaigns,
    campaign_api_create,
    campaign_api_delete,
    campaign_api_get,
    campaign_api_update,
)

server_name = "FacebookCampaign"
instructions = """
Campaign MCP Server for Facebook Business API.

Provides typed access to all Campaign operations including:
- CRUD operations (create, read, update, delete)
- Ad Sets management
- Ads management
- Campaign copying

Note: Insights operations are now in the dedicated Insights server.
"""

# Initialize server
server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
# CRUD operations
server.tool(campaign_api_get)
server.tool(campaign_api_create)
server.tool(campaign_api_update)
server.tool(campaign_api_delete)
server.tool(adaccount_get_campaigns)
server.tool(adaccount_delete_campaigns)

# Ad Sets operations
server.tool(campaign_get_ad_sets)
server.tool(campaign_create_budget_schedule)

# Ads operations
server.tool(campaign_get_ads)
server.tool(campaign_create_ad_label)
server.tool(campaign_get_ad_rules_governed)


# Copy operations
server.tool(campaign_get_copies)
server.tool(campaign_create_copy)
