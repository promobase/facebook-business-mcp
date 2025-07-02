"""OfflineProductItem MCP Server with typed wrappers."""

from facebook_business.adobjects.offlineproductitem import OfflineProductItem
from fastmcp import FastMCP

from src.generated.models.offlineproductitem import (
    OfflineProductItemField,
    OfflineProductItemGetOverrideDetailsParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOfflineProductItem"
instructions = """
OfflineProductItem MCP Server for Facebook Business API.

Provides typed access to all OfflineProductItem operations.
"""

offlineproductitem_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offlineproductitem_server.tool
@wrapped_fn_tool
def get_offlineproductitem(
    offlineproductitem_id: str,
    fields: list[OfflineProductItemField] = [],
) -> str:
    """Get a OfflineProductItem object by ID.

    Args:
        offlineproductitem_id: The ID of the OfflineProductItem.
        fields: Fields to retrieve. Available fields: See OfflineProductItemField type.
    """
    obj = OfflineProductItem(offlineproductitem_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@offlineproductitem_server.tool
@wrapped_fn_tool
def get_override_details(
    offlineproductitem_id: str,
    fields: list[OverrideDetailsField] = [],
    params: OfflineProductItemGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this OfflineProductItem.

    Args:
        offlineproductitem_id: The ID of the OfflineProductItem.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See OfflineProductItemGetOverrideDetailsParams type.
    """
    return OfflineProductItem(offlineproductitem_id).get_override_details(
        fields=fields, params=params
    )
