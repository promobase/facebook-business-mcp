"""
Auto-generated MCP server for Facebook TaggableSubject.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.taggablesubject import TaggableSubject
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-taggablesubject")


# CRUD Operations


@mcp.tool()
async def api_create_taggablesubject(
    taggablesubject_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TaggableSubject(fbid=taggablesubject_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_taggablesubject(
    taggablesubject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TaggableSubject(fbid=taggablesubject_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_taggablesubject(
    taggablesubject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TaggableSubject(fbid=taggablesubject_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_taggablesubject(
    taggablesubject_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TaggableSubject(fbid=taggablesubject_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
taggablesubject_server = mcp
