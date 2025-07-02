"""
Auto-generated MCP server for Facebook CopyrightMediaMisuse.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.copyrightmediamisuse import CopyrightMediaMisuse
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-copyrightmediamisuse")


# CRUD Operations


@mcp.tool()
async def api_create_copyrightmediamisuse(
    copyrightmediamisuse_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightMediaMisuse(fbid=copyrightmediamisuse_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_copyrightmediamisuse(
    copyrightmediamisuse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightMediaMisuse(fbid=copyrightmediamisuse_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_copyrightmediamisuse(
    copyrightmediamisuse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightMediaMisuse(fbid=copyrightmediamisuse_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_copyrightmediamisuse(
    copyrightmediamisuse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CopyrightMediaMisuse(fbid=copyrightmediamisuse_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
copyrightmediamisuse_server = mcp
