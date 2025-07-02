"""
Auto-generated MCP server for Facebook FantasyGame.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fantasygame import FantasyGame
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-fantasygame")


# CRUD Operations


@mcp.tool()
async def api_create_fantasygame(
    fantasygame_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FantasyGame(fbid=fantasygame_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_fantasygame(
    fantasygame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FantasyGame(fbid=fantasygame_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_fantasygame(
    fantasygame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FantasyGame(fbid=fantasygame_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_fantasygame(
    fantasygame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FantasyGame(fbid=fantasygame_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fantasygame_server = mcp
