"""
Auto-generated MCP server for Facebook CallAdsPhoneData.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.calladsphonedata import CallAdsPhoneData
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-calladsphonedata")


# CRUD Operations


@mcp.tool()
async def get_calladsphonedata(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CallAdsPhoneData.

    Args:
        object_id: The ID of the CallAdsPhoneData
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CallAdsPhoneData(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
calladsphonedata_server = mcp
