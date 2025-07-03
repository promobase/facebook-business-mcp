"""
Auto-generated MCP server for Facebook PlaceTopic.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.placetopic import PlaceTopic
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-placetopic")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    placetopic_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTopic(fbid=placetopic_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    placetopic_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTopic(fbid=placetopic_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    placetopic_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTopic(fbid=placetopic_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    placetopic_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlaceTopic(fbid=placetopic_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
placetopic_server = mcp
