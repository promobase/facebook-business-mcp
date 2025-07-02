"""
Auto-generated MCP server for Facebook DraftPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.draftpost import DraftPost
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-draftpost")


# CRUD Operations


@mcp.tool()
async def api_create_draftpost(
    draftpost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DraftPost(fbid=draftpost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_draftpost(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DraftPost(fbid=draftpost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_draftpost(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DraftPost(fbid=draftpost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_draftpost(
    draftpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DraftPost(fbid=draftpost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
draftpost_server = mcp
