"""
Auto-generated MCP server for Facebook ThirdPartyPartnerLiftRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartypartnerliftrequest import ThirdPartyPartnerLiftRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartypartnerliftrequest")


# CRUD Operations


@mcp.tool()
async def get_thirdpartypartnerliftrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ThirdPartyPartnerLiftRequest.

    Args:
        object_id: The ID of the ThirdPartyPartnerLiftRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ThirdPartyPartnerLiftRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartypartnerliftrequest_server = mcp
