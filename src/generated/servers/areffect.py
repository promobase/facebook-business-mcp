"""
Auto-generated MCP server for Facebook AREffect.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.areffect import AREffect
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-areffect")


# CRUD Operations


@mcp.tool()
async def get_areffect(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AREffect.

    Args:
        object_id: The ID of the AREffect
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AREffect(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
areffect_server = mcp
