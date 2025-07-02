"""ShadowIGHashtag MCP Server."""

from typing import Any

from facebook_business.adobjects.shadowighashtag import ShadowIGHashtag
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookShadowIGHashtag"
instructions = """
ShadowIGHashtag MCP Server for Facebook Business API.

Provides typed access to all ShadowIGHashtag operations.
"""

shadowighashtag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@shadowighashtag_server.tool
@wrapped_fn_tool
def get_shadowighashtag(
    shadowighashtag_id: str,
    fields: list[str] = [],
) -> str:
    obj = ShadowIGHashtag(shadowighashtag_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@shadowighashtag_server.tool
@wrapped_fn_tool
def get_recent_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ShadowIGHashtag(shadowighashtag_id).get_recent_media(fields=fields, params=params)


@shadowighashtag_server.tool
@wrapped_fn_tool
def get_top_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ShadowIGHashtag(shadowighashtag_id).get_top_media(fields=fields, params=params)
