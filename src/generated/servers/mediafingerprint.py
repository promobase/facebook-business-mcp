"""
Auto-generated MCP server for Facebook MediaFingerprint.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediafingerprint import MediaFingerprint
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mediafingerprint")


# CRUD Operations


@mcp.tool()
async def api_create_mediafingerprint(
    mediafingerprint_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_mediafingerprint(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediafingerprint_server = mcp
