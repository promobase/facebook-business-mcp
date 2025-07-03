"""
Auto-generated MCP server for Facebook CommerceOrder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commerceorder import CommerceOrder
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-commerceorder")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    commerceorder_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_acknowledge_order(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_acknowledge_order(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_cancellation(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_cancellation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_item_update(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_item_update(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_refund(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_refund(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_return(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_return(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_shipment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_update_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).create_update_shipment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_cancellations(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_cancellations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_items(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_items(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_payments(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_payments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_promo_t_i_ons(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_promo_t_i_ons(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_promotion_details(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_promotion_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_refunds(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_refunds(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_returns(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_returns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shipments(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceOrder(fbid=commerceorder_id).get_shipments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commerceorder_server = mcp
