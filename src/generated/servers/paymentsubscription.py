"""PaymentSubscription MCP Server."""

from typing import Any

from facebook_business.adobjects.paymentsubscription import PaymentSubscription
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPaymentSubscription"
instructions = """
PaymentSubscription MCP Server for Facebook Business API.

Provides typed access to all PaymentSubscription operations.
"""

paymentsubscription_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@paymentsubscription_server.tool
@wrapped_fn_tool
def get_paymentsubscription(
    paymentsubscription_id: str,
    fields: list[str] = [],
) -> str:
    obj = PaymentSubscription(paymentsubscription_id)
    return obj.api_get(fields=fields)
