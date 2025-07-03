"""AdSet MCP Server configuration."""

from fastmcp import FastMCP

from .ads import (
    adset_create_ad_label,
    adset_delete_ad_labels,
    adset_get_ad_creatives,
    adset_get_ad_rules_governed,
    adset_get_ads,
)

# Import all adset operations
from .crud import (
    adset_api_create,
    adset_api_delete,
    adset_api_get,
    adset_api_update,
)
from .operations import (
    adset_create_budget_schedule,
    adset_create_copy,
    adset_get_activities,
    adset_get_async_ad_requests,
    adset_get_copies,
)

server_name = "FacebookAdSet"
instructions = """
AdSet MCP Server for Facebook Business API.

Provides typed access to all AdSet operations including:
- CRUD operations (create, read, update, delete)
- Ads management within ad sets
- Budget scheduling
- Ad set copying

Note: Insights operations (including delivery estimates) are now in the dedicated Insights server.
"""

# Initialize server
server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
# CRUD operations
server.tool(adset_api_get)
server.tool(adset_api_create)
server.tool(adset_api_update)
server.tool(adset_api_delete)

# Ads operations
server.tool(adset_get_ads)
server.tool(adset_get_ad_creatives)
server.tool(adset_create_ad_label)
server.tool(adset_delete_ad_labels)
server.tool(adset_get_ad_rules_governed)


# Other operations
server.tool(adset_get_activities)
server.tool(adset_get_copies)
server.tool(adset_create_copy)
server.tool(adset_create_budget_schedule)
server.tool(adset_get_async_ad_requests)
