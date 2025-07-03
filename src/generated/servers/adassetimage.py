"""
Auto-generated MCP server for Facebook AdAssetImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetimage import AdAssetImage
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetimage")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adassetimage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAssetImage(fbid=adassetimage_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAssetImage(fbid=adassetimage_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAssetImage(fbid=adassetimage_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adassetimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAssetImage(fbid=adassetimage_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetimage_server = mcp
