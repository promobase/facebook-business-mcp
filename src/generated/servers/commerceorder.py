"""
Auto-generated MCP server for Facebook CommerceOrder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceorder import CommerceOrder
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceorder")


# CRUD Operations


@mcp.tool()
async def get_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CommerceOrder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_acknowledge_order_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Acknowledge Order for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_acknowledge_order result
    """
    result = CommerceOrder(fbid=object_id).create_acknowledge_order(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_cancellation_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Cancellation for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_cancellation result
    """
    result = CommerceOrder(fbid=object_id).create_cancellation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_item_update_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Item Update for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_item_update result
    """
    result = CommerceOrder(fbid=object_id).create_item_update(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_refund_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Refund for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_refund result
    """
    result = CommerceOrder(fbid=object_id).create_refund(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_return_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Return for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_return result
    """
    result = CommerceOrder(fbid=object_id).create_return(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shipment_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Shipment for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_shipment result
    """
    result = CommerceOrder(fbid=object_id).create_shipment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_update_shipment_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Update Shipment for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_update_shipment result
    """
    result = CommerceOrder(fbid=object_id).create_update_shipment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cancellations_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Cancellations for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_cancellations result
    """
    result = CommerceOrder(fbid=object_id).get_cancellations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_items_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Items for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_items result
    """
    result = CommerceOrder(fbid=object_id).get_items(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_payments_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Payments for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_payments result
    """
    result = CommerceOrder(fbid=object_id).get_payments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_promo_t_i_ons_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Promo T I Ons for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_promo_t_i_ons result
    """
    result = CommerceOrder(fbid=object_id).get_promo_t_i_ons(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_promotion_details_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Promotion Details for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_promotion_details result
    """
    result = CommerceOrder(fbid=object_id).get_promotion_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_refunds_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Refunds for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_refunds result
    """
    result = CommerceOrder(fbid=object_id).get_refunds(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_returns_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Returns for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_returns result
    """
    result = CommerceOrder(fbid=object_id).get_returns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shipments_for_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shipments for CommerceOrder.

    Args:
        object_id: The ID of the CommerceOrder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shipments result
    """
    result = CommerceOrder(fbid=object_id).get_shipments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceorder_server = mcp
