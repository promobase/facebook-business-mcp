"""CreditCard MCP Server."""

from typing import Any

from facebook_business.adobjects.creditcard import CreditCard
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = CreditCard(creditcard_id)
    return obj.api_get(fields=fields)
