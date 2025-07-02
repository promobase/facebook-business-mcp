"""
Auto-generated MCP server for Facebook ThirdPartyPartnerViewabilityRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartypartnerviewabilityrequest import (
    ThirdPartyPartnerViewabilityRequest,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartypartnerviewabilityrequest")


# CRUD Operations


@mcp.tool()
async def get_thirdpartypartnerviewabilityrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ThirdPartyPartnerViewabilityRequest.

    Args:
        object_id: The ID of the ThirdPartyPartnerViewabilityRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ThirdPartyPartnerViewabilityRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartypartnerviewabilityrequest_server = mcp
