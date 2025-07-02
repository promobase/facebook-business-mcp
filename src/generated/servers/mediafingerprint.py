"""MediaFingerprint MCP Server."""

from typing import Any

from facebook_business.adobjects.mediafingerprint import MediaFingerprint
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaFingerprint"
instructions = """
MediaFingerprint MCP Server for Facebook Business API.

Provides typed access to all MediaFingerprint operations.
"""

mediafingerprint_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@mediafingerprint_server.tool
@wrapped_fn_tool
def get_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[str] = [],
) -> str:
    obj = MediaFingerprint(mediafingerprint_id)
    return obj.api_get(fields=fields)


@mediafingerprint_server.tool
@wrapped_fn_tool
def update_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return MediaFingerprint(mediafingerprint_id).api_update(fields=fields, params=params)
