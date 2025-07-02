"""
Auto-generated MCP server for Facebook ShadowIGHashtag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowighashtag import ShadowIGHashtag
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowighashtag")


# CRUD Operations


@mcp.tool()
async def api_create_shadowighashtag(
    shadowighashtag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_shadowighashtag(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_shadowighashtag(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_shadowighashtag(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_recent_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_top_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).get_top_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowighashtag_server = mcp
