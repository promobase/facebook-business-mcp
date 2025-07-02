"""TransactableItem MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.transactableitem import TransactableItem
from fastmcp import FastMCP

from src.generated.models.overridedetails import OverrideDetailsField
from src.generated.models.transactableitem import (
    TransactableItemField,
    TransactableItemGetOverrideDetailsParams,
)
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
    fields: list[TransactableItemField] = [],
) -> str:
    """Get a TransactableItem object by ID.

    Args:
        transactableitem_id: The ID of the TransactableItem.
        fields: Fields to retrieve. Available fields: See TransactableItemField type.
    """
    obj = TransactableItem(transactableitem_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@transactableitem_server.tool
@wrapped_fn_tool
def get_override_details(
    transactableitem_id: str,
    fields: list[OverrideDetailsField] = [],
    params: TransactableItemGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this TransactableItem.

    Args:
        transactableitem_id: The ID of the TransactableItem.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See TransactableItemGetOverrideDetailsParams type.
    """
    return TransactableItem(transactableitem_id).get_override_details(fields=fields, params=params)
