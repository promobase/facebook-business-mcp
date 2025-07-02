"""TransactableItem MCP Server."""

from typing import Any

from facebook_business.adobjects.transactableitem import TransactableItem
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookTransactableItem"
instructions = """
TransactableItem MCP Server for Facebook Business API.

Provides typed access to all TransactableItem operations.
"""

transactableitem_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@transactableitem_server.tool
@wrapped_fn_tool
def get_transactableitem(
    transactableitem_id: str,
    fields: list[str] = [],
) -> str:
    obj = TransactableItem(transactableitem_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@transactableitem_server.tool
@wrapped_fn_tool
def get_override_details(
    transactableitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return TransactableItem(transactableitem_id).get_override_details(fields=fields, params=params)
