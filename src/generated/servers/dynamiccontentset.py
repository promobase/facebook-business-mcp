"""
Auto-generated MCP server for Facebook DynamicContentSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamiccontentset import DynamicContentSet
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamiccontentset")


# CRUD Operations


@mcp.tool()
async def get_dynamiccontentset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a DynamicContentSet.

    Args:
        object_id: The ID of the DynamicContentSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = DynamicContentSet(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamiccontentset_server = mcp
