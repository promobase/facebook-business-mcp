"""AdAccount MCP Server configuration."""

from fastmcp import FastMCP

from .ad_creatives import get_ad_creatives
from .ad_sets import get_ad_sets
from .ads import get_ads
from .campaigns import delete_campaigns, get_campaigns
from .crud import api_get, api_update

server_name = "FacebookAdAccount"
instructions = """
AdAccount MCP Server for Facebook Business API.

Provides typed access to AdAccount-level operations:
- Get account details (api_get, api_update)
- List campaigns, ad sets, ads, and ad creatives
- Delete campaigns in bulk

Note: Create operations for campaigns, ad sets, ads, and ad creatives 
are now in their respective dedicated servers.
"""

adaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
adaccount_server.tool(api_get)
adaccount_server.tool(api_update)
adaccount_server.tool(get_campaigns)
adaccount_server.tool(delete_campaigns)
adaccount_server.tool(get_ad_sets)
adaccount_server.tool(get_ads)
adaccount_server.tool(get_ad_creatives)
