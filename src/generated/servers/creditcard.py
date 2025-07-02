"""
Auto-generated MCP server for Facebook CreditCard.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.creditcard import CreditCard
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-creditcard")


# CRUD Operations


@mcp.tool()
async def get_creditcard(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CreditCard.

    Args:
        object_id: The ID of the CreditCard
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CreditCard(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
creditcard_server = mcp
