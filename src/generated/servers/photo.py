"""Photo MCP Server."""

from typing import Any

from facebook_business.adobjects.photo import Photo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPhoto"
instructions = """
Photo MCP Server for Facebook Business API.

Provides typed access to all Photo operations.
"""

photo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@photo_server.tool
@wrapped_fn_tool
def get_photo(
    photo_id: str,
    fields: list[str] = [],
) -> str:
    obj = Photo(photo_id)
    return obj.api_get(fields=fields)


@photo_server.tool
@wrapped_fn_tool
def delete_photo(
    photo_id: str,
) -> str:
    return Photo(photo_id).api_delete()


# ---- Edge Methods (6) ----
@photo_server.tool
@wrapped_fn_tool
def get_comments(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).get_comments(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def create_comment(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).create_comment(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def get_insights(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).get_insights(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def get_likes(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).get_likes(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def create_like(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).create_like(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def get_sponsor_tags(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Photo(photo_id).get_sponsor_tags(fields=fields, params=params)
