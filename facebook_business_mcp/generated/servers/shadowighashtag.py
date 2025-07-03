"""
Auto-generated MCP server for Facebook ShadowIGHashtag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowighashtag import ShadowIGHashtag
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowighashtag")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    shadowighashtag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_recent_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_top_media(
    shadowighashtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGHashtag(fbid=shadowighashtag_id).get_top_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowighashtag_server = mcp
