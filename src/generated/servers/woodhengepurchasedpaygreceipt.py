"""
Auto-generated MCP server for Facebook WoodhengePurchasedPAYGReceipt.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceipt
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-woodhengepurchasedpaygreceipt")


# CRUD Operations


@mcp.tool()
async def get_woodhengepurchasedpaygreceipt(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WoodhengePurchasedPAYGReceipt.

    Args:
        object_id: The ID of the WoodhengePurchasedPAYGReceipt
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WoodhengePurchasedPAYGReceipt(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
woodhengepurchasedpaygreceipt_server = mcp
