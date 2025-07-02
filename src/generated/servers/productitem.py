"""ProductItem MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productitem import ProductItem
from fastmcp import FastMCP

from src.generated.models.overridedetails import OverrideDetailsField
from src.generated.models.productitem import (
    ProductItemField,
    ProductItemGetOverrideDetailsParams,
    ProductItemUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductItem"
instructions = """
ProductItem MCP Server for Facebook Business API.

Provides typed access to all ProductItem operations.
"""

productitem_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productitem_server.tool
@wrapped_fn_tool
def get_productitem(
    productitem_id: str,
    fields: list[ProductItemField] = [],
) -> str:
    """Get a ProductItem object by ID.

    Args:
        productitem_id: The ID of the ProductItem.
        fields: Fields to retrieve. Available fields: See ProductItemField type.
    """
    obj = ProductItem(productitem_id)
    return obj.api_get(fields=fields)


@productitem_server.tool
@wrapped_fn_tool
def update_productitem(
    productitem_id: str,
    fields: list[ProductItemField] = [],
    params: ProductItemUpdateParams | dict = {},
) -> str:
    """Update a ProductItem object.

    Args:
        productitem_id: The ID of the ProductItem.
        fields: Fields to return after update. Available fields: See ProductItemField type.
        params: Parameters to update. Available params: See ProductItemUpdateParams type.
    """
    return ProductItem(productitem_id).api_update(fields=fields, params=params)


@productitem_server.tool
@wrapped_fn_tool
def delete_productitem(
    productitem_id: str,
) -> str:
    """Delete a ProductItem object.

    Args:
        productitem_id: The ID of the ProductItem.
    """
    return ProductItem(productitem_id).api_delete()


# ---- Edge Methods (1) ----
@productitem_server.tool
@wrapped_fn_tool
def get_override_details(
    productitem_id: str,
    fields: list[OverrideDetailsField] = [],
    params: ProductItemGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this ProductItem.

    Args:
        productitem_id: The ID of the ProductItem.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See ProductItemGetOverrideDetailsParams type.
    """
    return ProductItem(productitem_id).get_override_details(fields=fields, params=params)
