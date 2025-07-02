"""
Auto-generated MCP server for Facebook OmegaCustomerTrx.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.omegacustomertrx import OmegaCustomerTrx
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-omegacustomertrx")


# CRUD Operations


@mcp.tool()
async def get_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OmegaCustomerTrx.

    Args:
        object_id: The ID of the OmegaCustomerTrx
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OmegaCustomerTrx(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_campaigns_for_omegacustomertrx(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Campaigns for OmegaCustomerTrx.

    Args:
        object_id: The ID of the OmegaCustomerTrx
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_campaigns result
    """
    result = OmegaCustomerTrx(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
omegacustomertrx_server = mcp
