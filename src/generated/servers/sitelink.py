"""SiteLink MCP Server."""

from typing import Any

from facebook_business.adobjects.sitelink import SiteLink
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSiteLink"
instructions = """
SiteLink MCP Server for Facebook Business API.

Provides typed access to all SiteLink operations.
"""

sitelink_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@sitelink_server.tool
@wrapped_fn_tool
def get_sitelink(
    sitelink_id: str,
    fields: list[str] = [],
) -> str:
    obj = SiteLink(sitelink_id)
    return obj.api_get(fields=fields)
