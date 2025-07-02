"""Link MCP Server."""

from typing import Any

from facebook_business.adobjects.link import Link
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLink"
instructions = """
Link MCP Server for Facebook Business API.

Provides typed access to all Link operations.
"""

link_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@link_server.tool
@wrapped_fn_tool
def get_link(
    link_id: str,
    fields: list[str] = [],
) -> str:
    obj = Link(link_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@link_server.tool
@wrapped_fn_tool
def create_comment(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Link(link_id).create_comment(fields=fields, params=params)


@link_server.tool
@wrapped_fn_tool
def get_likes(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Link(link_id).get_likes(fields=fields, params=params)
