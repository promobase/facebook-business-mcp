"""
Auto-generated MCP server for Facebook ArAdsDataContainer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.aradsdatacontainer import ArAdsDataContainer
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-aradsdatacontainer")


# CRUD Operations


@mcp.tool()
async def get_aradsdatacontainer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ArAdsDataContainer.

    Args:
        object_id: The ID of the ArAdsDataContainer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ArAdsDataContainer(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
aradsdatacontainer_server = mcp
