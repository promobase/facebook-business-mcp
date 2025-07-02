"""WoodhengePurchasedPAYGReceipt MCP Server."""

from typing import Any

from facebook_business.adobjects.woodhengepurchasedpaygreceipt import WoodhengePurchasedPAYGReceipt
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWoodhengePurchasedPAYGReceipt"
instructions = """
WoodhengePurchasedPAYGReceipt MCP Server for Facebook Business API.

Provides typed access to all WoodhengePurchasedPAYGReceipt operations.
"""

woodhengepurchasedpaygreceipt_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@woodhengepurchasedpaygreceipt_server.tool
@wrapped_fn_tool
def get_woodhengepurchasedpaygreceipt(
    woodhengepurchasedpaygreceipt_id: str,
    fields: list[str] = [],
) -> str:
    obj = WoodhengePurchasedPAYGReceipt(woodhengepurchasedpaygreceipt_id)
    return obj.api_get(fields=fields)
