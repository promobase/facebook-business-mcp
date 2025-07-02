"""
Auto-generated MCP server for Facebook CloudGame.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cloudgame import CloudGame
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cloudgame")


# CRUD Operations


@mcp.tool()
async def api_create_cloudgame(
    cloudgame_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CloudGame(fbid=cloudgame_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_cloudgame(
    cloudgame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CloudGame(fbid=cloudgame_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_cloudgame(
    cloudgame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CloudGame(fbid=cloudgame_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_cloudgame(
    cloudgame_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CloudGame(fbid=cloudgame_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cloudgame_server = mcp
