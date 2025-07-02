"""ArAdsDataContainer MCP Server."""

from typing import Any

from facebook_business.adobjects.aradsdatacontainer import ArAdsDataContainer
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookArAdsDataContainer"
instructions = """
ArAdsDataContainer MCP Server for Facebook Business API.

Provides typed access to all ArAdsDataContainer operations.
"""

aradsdatacontainer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@aradsdatacontainer_server.tool
@wrapped_fn_tool
def get_aradsdatacontainer(
    aradsdatacontainer_id: str,
    fields: list[str] = [],
) -> str:
    obj = ArAdsDataContainer(aradsdatacontainer_id)
    return obj.api_get(fields=fields)
