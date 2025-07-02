"""
Auto-generated MCP server for Facebook CRMAddress.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.crmaddress import CRMAddress
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-crmaddress")


# CRUD Operations


@mcp.tool()
async def get_crmaddress(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CRMAddress.

    Args:
        object_id: The ID of the CRMAddress
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CRMAddress(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
crmaddress_server = mcp
