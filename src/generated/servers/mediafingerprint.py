"""
Auto-generated MCP server for Facebook MediaFingerprint.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediafingerprint import MediaFingerprint
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-mediafingerprint")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    mediafingerprint_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    mediafingerprint_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MediaFingerprint(fbid=mediafingerprint_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediafingerprint_server = mcp
