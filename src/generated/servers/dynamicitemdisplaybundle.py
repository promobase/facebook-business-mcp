"""
Auto-generated MCP server for Facebook DynamicItemDisplayBundle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicitemdisplaybundle import DynamicItemDisplayBundle
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicitemdisplaybundle")


# CRUD Operations


@mcp.tool()
async def api_create_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundle(fbid=dynamicitemdisplaybundle_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundle(fbid=dynamicitemdisplaybundle_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundle(fbid=dynamicitemdisplaybundle_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundle(fbid=dynamicitemdisplaybundle_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicitemdisplaybundle_server = mcp
