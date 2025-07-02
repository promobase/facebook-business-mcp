"""
Auto-generated MCP server for Facebook WoodhengeSupporter.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.woodhengesupporter import WoodhengeSupporter
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-woodhengesupporter")


# CRUD Operations


@mcp.tool()
async def get_woodhengesupporter(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WoodhengeSupporter.

    Args:
        object_id: The ID of the WoodhengeSupporter
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WoodhengeSupporter(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
woodhengesupporter_server = mcp
