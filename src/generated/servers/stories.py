"""
Auto-generated MCP server for Facebook Stories.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.stories import Stories
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-stories")


# CRUD Operations


@mcp.tool()
async def api_create_stories(
    stories_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Stories(fbid=stories_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_stories(
    stories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Stories(fbid=stories_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_stories(
    stories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Stories(fbid=stories_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_stories(
    stories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Stories(fbid=stories_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_insights(
    stories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Stories(fbid=stories_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
stories_server = mcp
