"""
Auto-generated MCP server for Facebook AudioVisualReferenceMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiovisualreferencematch import AudioVisualReferenceMatch
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audiovisualreferencematch")


# CRUD Operations


@mcp.tool()
async def api_create_audiovisualreferencematch(
    audiovisualreferencematch_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioVisualReferenceMatch(fbid=audiovisualreferencematch_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_audiovisualreferencematch(
    audiovisualreferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioVisualReferenceMatch(fbid=audiovisualreferencematch_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_audiovisualreferencematch(
    audiovisualreferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioVisualReferenceMatch(fbid=audiovisualreferencematch_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_audiovisualreferencematch(
    audiovisualreferencematch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioVisualReferenceMatch(fbid=audiovisualreferencematch_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiovisualreferencematch_server = mcp
