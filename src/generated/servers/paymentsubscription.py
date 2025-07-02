"""
Auto-generated MCP server for Facebook PaymentSubscription.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.paymentsubscription import PaymentSubscription
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-paymentsubscription")


# CRUD Operations


@mcp.tool()
async def get_paymentsubscription(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PaymentSubscription.

    Args:
        object_id: The ID of the PaymentSubscription
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PaymentSubscription(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentsubscription_server = mcp
