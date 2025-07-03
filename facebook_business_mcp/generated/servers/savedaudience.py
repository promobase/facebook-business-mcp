"""
Auto-generated MCP server for Facebook SavedAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.savedaudience import SavedAudience
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-savedaudience")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    savedaudience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SavedAudience(fbid=savedaudience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    savedaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SavedAudience(fbid=savedaudience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    savedaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SavedAudience(fbid=savedaudience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    savedaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SavedAudience(fbid=savedaudience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
savedaudience_server = mcp
