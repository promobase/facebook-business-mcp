"""
Auto-generated MCP server for Facebook PlaceTopic.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.placetopic import PlaceTopic
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-placetopic")


# CRUD Operations


@mcp.tool()
async def create_placetopic(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTopic(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_placetopic(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTopic(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_placetopic(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTopic(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_placetopic(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTopic(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
placetopic_server = mcp
