"""
Auto-generated MCP server for Facebook RawCustomAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rawcustomaudience import RawCustomAudience
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-rawcustomaudience")


# CRUD Operations


@mcp.tool()
async def api_create_rawcustomaudience(
    rawcustomaudience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RawCustomAudience(fbid=rawcustomaudience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_rawcustomaudience(
    rawcustomaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RawCustomAudience(fbid=rawcustomaudience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_rawcustomaudience(
    rawcustomaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RawCustomAudience(fbid=rawcustomaudience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_rawcustomaudience(
    rawcustomaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RawCustomAudience(fbid=rawcustomaudience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rawcustomaudience_server = mcp
