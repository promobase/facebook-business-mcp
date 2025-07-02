"""PaymentEnginePayment MCP Server."""

from typing import Any

from facebook_business.adobjects.paymentenginepayment import PaymentEnginePayment
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = PaymentEnginePayment(paymentenginepayment_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@paymentenginepayment_server.tool
@wrapped_fn_tool
def create_dispute(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PaymentEnginePayment(paymentenginepayment_id).create_dispute(
        fields=fields, params=params
    )


@paymentenginepayment_server.tool
@wrapped_fn_tool
def create_refund(
    paymentenginepayment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PaymentEnginePayment(paymentenginepayment_id).create_refund(fields=fields, params=params)
