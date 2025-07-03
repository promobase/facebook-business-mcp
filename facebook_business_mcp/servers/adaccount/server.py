"""AdAccount MCP Server configuration."""

from fastmcp import FastMCP

from .ad_sets import adaccount_get_ad_sets
from .crud import adaccount_api_get, adaccount_api_update

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
adaccount_server.tool(adaccount_api_get)
adaccount_server.tool(adaccount_api_update)
adaccount_server.tool(adaccount_get_ad_sets)
