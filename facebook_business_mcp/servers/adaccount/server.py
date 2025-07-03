"""AdAccount MCP Server configuration."""

from fastmcp import FastMCP

from .ad_creatives import create_ad_creative, get_ad_creatives
from .ad_sets import create_ad_set, get_ad_sets
from .ads import create_ad, get_ads
from .campaigns import create_campaign, delete_campaigns, get_campaigns
from .crud import api_get, api_update

server_name = "FacebookAdAccount"
instructions = """
AdAccount MCP Server for Facebook Business API.

Provides typed access to all AdAccount operations.
"""

adaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
adaccount_server.tool(api_get)
adaccount_server.tool(api_update)
adaccount_server.tool(get_campaigns)
adaccount_server.tool(create_campaign)
adaccount_server.tool(delete_campaigns)
adaccount_server.tool(get_ad_sets)
adaccount_server.tool(create_ad_set)
adaccount_server.tool(get_ads)
adaccount_server.tool(create_ad)
adaccount_server.tool(get_ad_creatives)
adaccount_server.tool(create_ad_creative)
