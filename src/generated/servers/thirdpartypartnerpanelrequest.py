"""
Auto-generated MCP server for Facebook ThirdPartyPartnerPanelRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartypartnerpanelrequest import ThirdPartyPartnerPanelRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartypartnerpanelrequest")


# CRUD Operations


@mcp.tool()
async def get_thirdpartypartnerpanelrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ThirdPartyPartnerPanelRequest.

    Args:
        object_id: The ID of the ThirdPartyPartnerPanelRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ThirdPartyPartnerPanelRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartypartnerpanelrequest_server = mcp
