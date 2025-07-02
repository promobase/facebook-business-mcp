"""
Auto-generated MCP server for Facebook BusinessCreative.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesscreative import BusinessCreative
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesscreative")


# CRUD Operations


@mcp.tool()
async def api_create_businesscreative(
    businesscreative_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreative(fbid=businesscreative_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businesscreative(
    businesscreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreative(fbid=businesscreative_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businesscreative(
    businesscreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreative(fbid=businesscreative_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businesscreative(
    businesscreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreative(fbid=businesscreative_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesscreative_server = mcp
