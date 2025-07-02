"""PaymentEnginePayment MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.paymentenginepayment import PaymentEnginePayment
from fastmcp import FastMCP

from src.generated.models.paymentenginepayment import (
    PaymentEnginePaymentCreateDisputeParams,
    PaymentEnginePaymentCreateRefundParams,
    PaymentEnginePaymentField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPaymentEnginePayment"
instructions = """
PaymentEnginePayment MCP Server for Facebook Business API.

Provides typed access to all PaymentEnginePayment operations.
"""

paymentenginepayment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@paymentenginepayment_server.tool
@wrapped_fn_tool
def get_paymentenginepayment(
    paymentenginepayment_id: str,
    fields: list[PaymentEnginePaymentField] = [],
) -> str:
    """Get a PaymentEnginePayment object by ID.

    Args:
        paymentenginepayment_id: The ID of the PaymentEnginePayment.
        fields: Fields to retrieve. Available fields: See PaymentEnginePaymentField type.
    """
    obj = PaymentEnginePayment(paymentenginepayment_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@paymentenginepayment_server.tool
@wrapped_fn_tool
def create_dispute(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: PaymentEnginePaymentCreateDisputeParams | dict = {},
):
    """Create Dispute for this PaymentEnginePayment.

    Args:
        paymentenginepayment_id: The ID of the PaymentEnginePayment.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PaymentEnginePaymentCreateDisputeParams type.
    """
    return PaymentEnginePayment(paymentenginepayment_id).create_dispute(
        fields=fields, params=params
    )


@paymentenginepayment_server.tool
@wrapped_fn_tool
def create_refund(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: PaymentEnginePaymentCreateRefundParams | dict = {},
):
    """Create Refund for this PaymentEnginePayment.

    Args:
        paymentenginepayment_id: The ID of the PaymentEnginePayment.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PaymentEnginePaymentCreateRefundParams type.
    """
    return PaymentEnginePayment(paymentenginepayment_id).create_refund(fields=fields, params=params)
