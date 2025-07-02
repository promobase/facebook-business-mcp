"""WebsiteCreativeInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.websitecreativeinfo import WebsiteCreativeInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWebsiteCreativeInfo"
instructions = """
WebsiteCreativeInfo MCP Server for Facebook Business API.

Provides typed access to all WebsiteCreativeInfo operations.
"""

websitecreativeinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@websitecreativeinfo_server.tool
@wrapped_fn_tool
def get_websitecreativeinfo(
    websitecreativeinfo_id: str,
    fields: list[str] = [],
) -> str:
    obj = WebsiteCreativeInfo(websitecreativeinfo_id)
    return obj.api_get(fields=fields)
