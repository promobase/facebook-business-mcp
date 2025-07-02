"""Post MCP Server."""

from typing import Any

from facebook_business.adobjects.post import Post
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPost"
instructions = """
Post MCP Server for Facebook Business API.

Provides typed access to all Post operations.
"""

post_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@post_server.tool
@wrapped_fn_tool
def get_post(
    post_id: str,
    fields: list[str] = [],
) -> str:
    obj = Post(post_id)
    return obj.api_get(fields=fields)


@post_server.tool
@wrapped_fn_tool
def update_post(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Post(post_id).api_update(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def delete_post(
    post_id: str,
) -> str:
    return Post(post_id).api_delete()


# ---- Edge Methods (11) ----
@post_server.tool
@wrapped_fn_tool
def get_attachments(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_attachments(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_comments(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_comments(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def create_comment(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).create_comment(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_dynamic_posts(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_dynamic_posts(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_insights(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_insights(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def delete_likes(
    post_id: str,
    params: dict[str, Any] = {},
):
    return Post(post_id).delete_likes(params=params)


@post_server.tool
@wrapped_fn_tool
def create_like(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).create_like(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_reactions(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_reactions(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_sharedposts(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_sharedposts(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_sponsor_tags(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_sponsor_tags(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_to(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Post(post_id).get_to(fields=fields, params=params)
