"""
Auto-generated MCP server for Facebook AdAssetImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetimage import AdAssetImage
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetimage")


# CRUD Operations


@mcp.tool()
async def api_create_adassetimage(
    adassetimage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetImage(fbid=adassetimage_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassetimage(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetImage(fbid=adassetimage_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassetimage(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetImage(fbid=adassetimage_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassetimage(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetImage(fbid=adassetimage_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetimage_server = mcp
