"""
Auto-generated MCP server for Facebook OfflineTermsOfService.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlinetermsofservice import OfflineTermsOfService
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlinetermsofservice")


# CRUD Operations


@mcp.tool()
async def get_offlinetermsofservice(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OfflineTermsOfService.

    Args:
        object_id: The ID of the OfflineTermsOfService
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OfflineTermsOfService(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlinetermsofservice_server = mcp
