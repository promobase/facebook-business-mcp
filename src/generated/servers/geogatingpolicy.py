"""
Auto-generated MCP server for Facebook GeoGatingPolicy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.geogatingpolicy import GeoGatingPolicy
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-geogatingpolicy")


# CRUD Operations


@mcp.tool()
async def get_geogatingpolicy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a GeoGatingPolicy.

    Args:
        object_id: The ID of the GeoGatingPolicy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = GeoGatingPolicy(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
geogatingpolicy_server = mcp
