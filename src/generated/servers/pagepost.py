"""PagePost MCP Server."""

from typing import Any

from facebook_business.adobjects.pagepost import PagePost
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPagePost"
instructions = """
PagePost MCP Server for Facebook Business API.

Provides typed access to all PagePost operations.
"""

pagepost_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@pagepost_server.tool
@wrapped_fn_tool
def get_pagepost(
    pagepost_id: str,
    fields: list[str] = [],
) -> str:
    obj = PagePost(pagepost_id)
    return obj.api_get(fields=fields)


@pagepost_server.tool
@wrapped_fn_tool
def update_pagepost(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return PagePost(pagepost_id).api_update(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def delete_pagepost(
    pagepost_id: str,
) -> str:
    return PagePost(pagepost_id).api_delete()


# ---- Edge Methods (6) ----
@pagepost_server.tool
@wrapped_fn_tool
def get_comments(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).get_comments(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def create_comment(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).create_comment(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def get_insights(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).get_insights(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def delete_likes(
    pagepost_id: str,
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).delete_likes(params=params)


@pagepost_server.tool
@wrapped_fn_tool
def create_like(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).create_like(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def get_reactions(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PagePost(pagepost_id).get_reactions(fields=fields, params=params)
