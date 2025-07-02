"""
Auto-generated MCP server for Facebook DynamicItemDisplayBundle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicitemdisplaybundle import DynamicItemDisplayBundle
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicitemdisplaybundle")


# CRUD Operations


@mcp.tool()
async def get_dynamicitemdisplaybundle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a DynamicItemDisplayBundle.

    Args:
        object_id: The ID of the DynamicItemDisplayBundle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = DynamicItemDisplayBundle(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicitemdisplaybundle_server = mcp
