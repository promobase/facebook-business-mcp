"""
Auto-generated MCP server for Facebook MediaCopyrightAttribution.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediacopyrightattribution import MediaCopyrightAttribution
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mediacopyrightattribution")


# CRUD Operations


@mcp.tool()
async def get_mediacopyrightattribution(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MediaCopyrightAttribution.

    Args:
        object_id: The ID of the MediaCopyrightAttribution
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MediaCopyrightAttribution(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediacopyrightattribution_server = mcp
