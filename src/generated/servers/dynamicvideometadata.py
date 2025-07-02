"""
Auto-generated MCP server for Facebook DynamicVideoMetadata.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicvideometadata import DynamicVideoMetadata
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicvideometadata")


# CRUD Operations


@mcp.tool()
async def get_dynamicvideometadata(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a DynamicVideoMetadata.

    Args:
        object_id: The ID of the DynamicVideoMetadata
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = DynamicVideoMetadata(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicvideometadata_server = mcp
