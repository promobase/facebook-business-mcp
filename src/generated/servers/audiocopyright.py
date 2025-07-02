"""
Auto-generated MCP server for Facebook AudioCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiocopyright import AudioCopyright
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audiocopyright")


# CRUD Operations


@mcp.tool()
async def get_audiocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AudioCopyright.

    Args:
        object_id: The ID of the AudioCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AudioCopyright(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_update_records_for_audiocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Update Records for AudioCopyright.

    Args:
        object_id: The ID of the AudioCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_update_records result
    """
    result = AudioCopyright(fbid=object_id).get_update_records(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiocopyright_server = mcp
