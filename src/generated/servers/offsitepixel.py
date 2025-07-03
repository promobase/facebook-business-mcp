"""
Auto-generated MCP server for Facebook OffsitePixel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offsitepixel import OffsitePixel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-offsitepixel")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    offsitepixel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OffsitePixel(fbid=offsitepixel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    offsitepixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OffsitePixel(fbid=offsitepixel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    offsitepixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OffsitePixel(fbid=offsitepixel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    offsitepixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OffsitePixel(fbid=offsitepixel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offsitepixel_server = mcp
