"""Album MCP Server."""

from typing import Any

from facebook_business.adobjects.album import Album
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAlbum"
instructions = """
Album MCP Server for Facebook Business API.

Provides typed access to all Album operations.
"""

album_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@album_server.tool
@wrapped_fn_tool
def get_album(
    album_id: str,
    fields: list[str] = [],
) -> str:
    obj = Album(album_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (5) ----
@album_server.tool
@wrapped_fn_tool
def get_comments(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Album(album_id).get_comments(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_comment(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Album(album_id).create_comment(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_like(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Album(album_id).create_like(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_photo(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Album(album_id).create_photo(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def get_picture(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Album(album_id).get_picture(fields=fields, params=params)
