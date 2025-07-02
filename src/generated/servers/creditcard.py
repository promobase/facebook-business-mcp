"""CreditCard MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.creditcard import CreditCard
from fastmcp import FastMCP

from src.generated.models.creditcard import CreditCardField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCreditCard"
instructions = """
CreditCard MCP Server for Facebook Business API.

Provides typed access to all CreditCard operations.
"""

creditcard_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@creditcard_server.tool
@wrapped_fn_tool
def get_creditcard(
    creditcard_id: str,
    fields: list[CreditCardField] = [],
) -> str:
    """Get a CreditCard object by ID.

    Args:
        creditcard_id: The ID of the CreditCard.
        fields: Fields to retrieve. Available fields: See CreditCardField type.
    """
    obj = CreditCard(creditcard_id)
    return obj.api_get(fields=fields)
