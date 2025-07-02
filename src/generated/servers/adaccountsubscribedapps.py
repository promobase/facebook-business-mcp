"""
Auto-generated MCP server for Facebook AdAccountSubscribedApps.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountsubscribedapps import AdAccountSubscribedApps
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountsubscribedapps")


# CRUD Operations


@mcp.tool()
async def create_adaccountsubscribedapps(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdAccountSubscribedApps.

    Args:
        object_id: The ID of the AdAccountSubscribedApps
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdAccountSubscribedApps(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountsubscribedapps_server = mcp
