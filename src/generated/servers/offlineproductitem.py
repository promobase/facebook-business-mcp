"""OfflineProductItem MCP Server."""

from typing import Any

from facebook_business.adobjects.offlineproductitem import OfflineProductItem
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = OfflineProductItem(offlineproductitem_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@offlineproductitem_server.tool
@wrapped_fn_tool
def get_override_details(
    offlineproductitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineProductItem(offlineproductitem_id).get_override_details(
        fields=fields, params=params
    )
