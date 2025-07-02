"""IGComment MCP Server."""

from typing import Any

from facebook_business.adobjects.igcomment import IGComment
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGComment"
instructions = """
IGComment MCP Server for Facebook Business API.

Provides typed access to all IGComment operations.
"""

igcomment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@igcomment_server.tool
@wrapped_fn_tool
def get_igcomment(
    igcomment_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGComment(igcomment_id)
    return obj.api_get(fields=fields)


@igcomment_server.tool
@wrapped_fn_tool
def update_igcomment(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return IGComment(igcomment_id).api_update(fields=fields, params=params)


@igcomment_server.tool
@wrapped_fn_tool
def delete_igcomment(
    igcomment_id: str,
) -> str:
    return IGComment(igcomment_id).api_delete()


# ---- Edge Methods (1) ----
@igcomment_server.tool
@wrapped_fn_tool
def create_reply(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGComment(igcomment_id).create_reply(fields=fields, params=params)
