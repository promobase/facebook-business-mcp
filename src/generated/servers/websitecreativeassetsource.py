"""WebsiteCreativeAssetSource MCP Server."""

from typing import Any

from facebook_business.adobjects.websitecreativeassetsource import WebsiteCreativeAssetSource
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWebsiteCreativeAssetSource"
instructions = """
WebsiteCreativeAssetSource MCP Server for Facebook Business API.

Provides typed access to all WebsiteCreativeAssetSource operations.
"""

websitecreativeassetsource_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@websitecreativeassetsource_server.tool
@wrapped_fn_tool
def get_websitecreativeassetsource(
    websitecreativeassetsource_id: str,
    fields: list[str] = [],
) -> str:
    obj = WebsiteCreativeAssetSource(websitecreativeassetsource_id)
    return obj.api_get(fields=fields)
