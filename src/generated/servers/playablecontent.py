"""
Auto-generated MCP server for Facebook PlayableContent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.playablecontent import PlayableContent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-playablecontent")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    playablecontent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlayableContent(fbid=playablecontent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    playablecontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlayableContent(fbid=playablecontent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    playablecontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlayableContent(fbid=playablecontent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    playablecontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PlayableContent(fbid=playablecontent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
playablecontent_server = mcp
