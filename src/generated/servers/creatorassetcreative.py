"""
Auto-generated MCP server for Facebook CreatorAssetCreative.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.creatorassetcreative import CreatorAssetCreative
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-creatorassetcreative")


# CRUD Operations


@mcp.tool()
async def api_create_creatorassetcreative(
    creatorassetcreative_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CreatorAssetCreative(fbid=creatorassetcreative_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_creatorassetcreative(
    creatorassetcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CreatorAssetCreative(fbid=creatorassetcreative_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_creatorassetcreative(
    creatorassetcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CreatorAssetCreative(fbid=creatorassetcreative_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_creatorassetcreative(
    creatorassetcreative_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CreatorAssetCreative(fbid=creatorassetcreative_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
creatorassetcreative_server = mcp
