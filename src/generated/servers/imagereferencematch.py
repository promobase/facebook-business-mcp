"""
Auto-generated MCP server for Facebook ImageReferenceMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.imagereferencematch import ImageReferenceMatch
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-imagereferencematch")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    imagereferencematch_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ImageReferenceMatch(fbid=imagereferencematch_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    imagereferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ImageReferenceMatch(fbid=imagereferencematch_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    imagereferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ImageReferenceMatch(fbid=imagereferencematch_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    imagereferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ImageReferenceMatch(fbid=imagereferencematch_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
imagereferencematch_server = mcp
