"""URL MCP Server."""

from typing import Any

from facebook_business.adobjects.url import URL
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookURL"
instructions = """
URL MCP Server for Facebook Business API.

Provides typed access to all URL operations.
"""

url_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@url_server.tool
@wrapped_fn_tool
def get_url(
    url_id: str,
    fields: list[str] = [],
) -> str:
    obj = URL(url_id)
    return obj.api_get(fields=fields)


@url_server.tool
@wrapped_fn_tool
def update_url(
    url_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return URL(url_id).api_update(fields=fields, params=params)
