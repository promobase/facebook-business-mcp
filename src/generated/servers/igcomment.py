"""
Auto-generated MCP server for Facebook IGComment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igcomment import IGComment
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igcomment")


# CRUD Operations


@mcp.tool()
async def api_create_igcomment(
    igcomment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igcomment(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igcomment(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igcomment(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_reply(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).create_reply(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_replies(
    igcomment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGComment(fbid=igcomment_id).get_replies(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igcomment_server = mcp
