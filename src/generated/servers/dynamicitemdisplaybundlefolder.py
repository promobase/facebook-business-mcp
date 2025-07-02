"""
Auto-generated MCP server for Facebook DynamicItemDisplayBundleFolder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicitemdisplaybundlefolder import (
    DynamicItemDisplayBundleFolder,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicitemdisplaybundlefolder")


# CRUD Operations


@mcp.tool()
async def get_dynamicitemdisplaybundlefolder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a DynamicItemDisplayBundleFolder.

    Args:
        object_id: The ID of the DynamicItemDisplayBundleFolder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = DynamicItemDisplayBundleFolder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicitemdisplaybundlefolder_server = mcp
