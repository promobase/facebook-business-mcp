"""Comment MCP Server."""

from typing import Any

from facebook_business.adobjects.comment import Comment
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookComment"
instructions = """
Comment MCP Server for Facebook Business API.

Provides typed access to all Comment operations.
"""

comment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@comment_server.tool
@wrapped_fn_tool
def get_comment(
    comment_id: str,
    fields: list[str] = [],
) -> str:
    obj = Comment(comment_id)
    return obj.api_get(fields=fields)


@comment_server.tool
@wrapped_fn_tool
def update_comment(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Comment(comment_id).api_update(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def delete_comment(
    comment_id: str,
) -> str:
    return Comment(comment_id).api_delete()


# ---- Edge Methods (6) ----
@comment_server.tool
@wrapped_fn_tool
def get_comments(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Comment(comment_id).get_comments(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def create_comment(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Comment(comment_id).create_comment(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def delete_likes(
    comment_id: str,
    params: dict[str, Any] = {},
):
    return Comment(comment_id).delete_likes(params=params)


@comment_server.tool
@wrapped_fn_tool
def get_likes(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Comment(comment_id).get_likes(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def create_like(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Comment(comment_id).create_like(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def get_reactions(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Comment(comment_id).get_reactions(fields=fields, params=params)
