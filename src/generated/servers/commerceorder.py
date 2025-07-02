"""
Auto-generated MCP server for Facebook CommerceOrder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceorder import CommerceOrder
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceorder")


# CRUD Operations


@mcp.tool()
async def create_commerceorder(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrder(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrder(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_commerceorder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceOrder(fbid=object_id).api_update(
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
    result = CommerceOrder(fbid=object_id).get_shipments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceorder_server = mcp
