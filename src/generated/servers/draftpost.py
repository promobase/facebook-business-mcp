"""
Auto-generated MCP server for Facebook DraftPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.draftpost import DraftPost
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-draftpost")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    draftpost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DraftPost(fbid=draftpost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DraftPost(fbid=draftpost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DraftPost(fbid=draftpost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DraftPost(fbid=draftpost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
draftpost_server = mcp
