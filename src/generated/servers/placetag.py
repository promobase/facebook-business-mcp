"""
Auto-generated MCP server for Facebook PlaceTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.placetag import PlaceTag
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-placetag")


# CRUD Operations


@mcp.tool()
async def api_create_placetag(
    placetag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTag(fbid=placetag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_placetag(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTag(fbid=placetag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_placetag(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTag(fbid=placetag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_placetag(
    placetag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PlaceTag(fbid=placetag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
placetag_server = mcp
