"""
Auto-generated MCP server for Facebook PaymentEnginePayment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.paymentenginepayment import PaymentEnginePayment
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-paymentenginepayment")


# CRUD Operations


@mcp.tool()
async def get_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PaymentEnginePayment.

    Args:
        object_id: The ID of the PaymentEnginePayment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PaymentEnginePayment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_dispute_for_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Dispute for PaymentEnginePayment.

    Args:
        object_id: The ID of the PaymentEnginePayment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_dispute result
    """
    result = PaymentEnginePayment(fbid=object_id).create_dispute(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_refund_for_paymentenginepayment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Refund for PaymentEnginePayment.

    Args:
        object_id: The ID of the PaymentEnginePayment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_refund result
    """
    result = PaymentEnginePayment(fbid=object_id).create_refund(
        fields=fields,
        params=params,
    )

    return result


# Export the server
paymentenginepayment_server = mcp
