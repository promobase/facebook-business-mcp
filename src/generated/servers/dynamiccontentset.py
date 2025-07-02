"""
Auto-generated MCP server for Facebook DynamicContentSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamiccontentset import DynamicContentSet
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamiccontentset")


# CRUD Operations


@mcp.tool()
async def api_create_dynamiccontentset(
    dynamiccontentset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicContentSet(fbid=dynamiccontentset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_dynamiccontentset(
    dynamiccontentset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicContentSet(fbid=dynamiccontentset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_dynamiccontentset(
    dynamiccontentset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicContentSet(fbid=dynamiccontentset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_dynamiccontentset(
    dynamiccontentset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicContentSet(fbid=dynamiccontentset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamiccontentset_server = mcp
