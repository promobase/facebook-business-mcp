"""
Auto-generated MCP server for Facebook AdAssetVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetvideo import AdAssetVideo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetvideo")


# CRUD Operations


@mcp.tool()
async def api_create_adassetvideo(
    adassetvideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetVideo(fbid=adassetvideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassetvideo(
    adassetvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetVideo(fbid=adassetvideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassetvideo(
    adassetvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetVideo(fbid=adassetvideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassetvideo(
    adassetvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetVideo(fbid=adassetvideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetvideo_server = mcp
