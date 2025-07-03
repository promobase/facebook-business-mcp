"""
Auto-generated MCP server for Facebook PlaceTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.placetag import PlaceTag
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-placetag")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    placetag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTag(fbid=placetag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTag(fbid=placetag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTag(fbid=placetag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTag(fbid=placetag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
placetag_server = mcp
