"""Transaction MCP Server."""

from typing import Any

from facebook_business.adobjects.transaction import Transaction
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookTransaction"
instructions = """
Transaction MCP Server for Facebook Business API.

Provides typed access to all Transaction operations.
"""

transaction_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@transaction_server.tool
@wrapped_fn_tool
def get_endpoint(
    transaction_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Transaction(transaction_id).get_endpoint(fields=fields, params=params)
