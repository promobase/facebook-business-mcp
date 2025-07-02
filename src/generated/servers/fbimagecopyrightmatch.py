"""
Auto-generated MCP server for Facebook FBImageCopyrightMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fbimagecopyrightmatch import FBImageCopyrightMatch
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-fbimagecopyrightmatch")


# CRUD Operations


@mcp.tool()
async def api_create_fbimagecopyrightmatch(
    fbimagecopyrightmatch_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FBImageCopyrightMatch(fbid=fbimagecopyrightmatch_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_fbimagecopyrightmatch(
    fbimagecopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FBImageCopyrightMatch(fbid=fbimagecopyrightmatch_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_fbimagecopyrightmatch(
    fbimagecopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FBImageCopyrightMatch(fbid=fbimagecopyrightmatch_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_fbimagecopyrightmatch(
    fbimagecopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FBImageCopyrightMatch(fbid=fbimagecopyrightmatch_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fbimagecopyrightmatch_server = mcp
