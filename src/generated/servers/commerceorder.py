"""CommerceOrder MCP Server with typed wrappers."""

from facebook_business.adobjects.commerceorder import CommerceOrder
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.commerceorder import (
    CommerceOrderCreateAcknowledgeOrderParams,
    CommerceOrderCreateCancellationParams,
    CommerceOrderCreateItemUpdateParams,
    CommerceOrderCreateRefundParams,
    CommerceOrderCreateReturnParams,
    CommerceOrderCreateShipmentParams,
    CommerceOrderCreateUpdateShipmentParams,
    CommerceOrderField,
    CommerceOrderGetReturnsParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCommerceOrder"
instructions = """
CommerceOrder MCP Server for Facebook Business API.

Provides typed access to all CommerceOrder operations.
"""

commerceorder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@commerceorder_server.tool
@wrapped_fn_tool
def get_commerceorder(
    commerceorder_id: str,
    fields: list[CommerceOrderField] = [],
) -> str:
    """Get a CommerceOrder object by ID.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve. Available fields: See CommerceOrderField type.
    """
    obj = CommerceOrder(commerceorder_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (8) ----
@commerceorder_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateAcknowledgeOrderParams | dict = {},
):
    """Create Acknowledge Order for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateAcknowledgeOrderParams type.
    """
    return CommerceOrder(commerceorder_id).create_acknowledge_order(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_cancellation(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateCancellationParams | dict = {},
):
    """Create Cancellation for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateCancellationParams type.
    """
    return CommerceOrder(commerceorder_id).create_cancellation(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_item_update(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateItemUpdateParams | dict = {},
):
    """Create Item Update for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateItemUpdateParams type.
    """
    return CommerceOrder(commerceorder_id).create_item_update(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_refund(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateRefundParams | dict = {},
):
    """Create Refund for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateRefundParams type.
    """
    return CommerceOrder(commerceorder_id).create_refund(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def get_returns(
    commerceorder_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: CommerceOrderGetReturnsParams | dict = {},
):
    """Get Returns for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See CommerceOrderGetReturnsParams type.
    """
    return CommerceOrder(commerceorder_id).get_returns(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_return(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateReturnParams | dict = {},
):
    """Create Return for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateReturnParams type.
    """
    return CommerceOrder(commerceorder_id).create_return(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateShipmentParams | dict = {},
):
    """Create Shipment for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateShipmentParams type.
    """
    return CommerceOrder(commerceorder_id).create_shipment(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_update_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: CommerceOrderCreateUpdateShipmentParams | dict = {},
):
    """Create Update Shipment for this CommerceOrder.

    Args:
        commerceorder_id: The ID of the CommerceOrder.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceOrderCreateUpdateShipmentParams type.
    """
    return CommerceOrder(commerceorder_id).create_update_shipment(fields=fields, params=params)
