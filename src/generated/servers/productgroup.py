"""ProductGroup MCP Server with typed wrappers."""

from facebook_business.adobjects.productgroup import ProductGroup
from fastmcp import FastMCP

from src.generated.models.productgroup import (
    ProductGroupCreateProductParams,
    ProductGroupField,
    ProductGroupUpdateParams,
)
from src.generated.models.productitem import ProductItemField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductGroup"
instructions = """
ProductGroup MCP Server for Facebook Business API.

Provides typed access to all ProductGroup operations.
"""

productgroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productgroup_server.tool
@wrapped_fn_tool
def get_productgroup(
    productgroup_id: str,
    fields: list[ProductGroupField] = [],
) -> str:
    """Get a ProductGroup object by ID.

    Args:
        productgroup_id: The ID of the ProductGroup.
        fields: Fields to retrieve. Available fields: See ProductGroupField type.
    """
    obj = ProductGroup(productgroup_id)
    return obj.api_get(fields=fields)


@productgroup_server.tool
@wrapped_fn_tool
def update_productgroup(
    productgroup_id: str,
    fields: list[ProductGroupField] = [],
    params: ProductGroupUpdateParams | dict = {},
) -> str:
    """Update a ProductGroup object.

    Args:
        productgroup_id: The ID of the ProductGroup.
        fields: Fields to return after update. Available fields: See ProductGroupField type.
        params: Parameters to update. Available params: See ProductGroupUpdateParams type.
    """
    return ProductGroup(productgroup_id).api_update(fields=fields, params=params)


@productgroup_server.tool
@wrapped_fn_tool
def delete_productgroup(
    productgroup_id: str,
) -> str:
    """Delete a ProductGroup object.

    Args:
        productgroup_id: The ID of the ProductGroup.
    """
    return ProductGroup(productgroup_id).api_delete()


# ---- Edge Methods (1) ----
@productgroup_server.tool
@wrapped_fn_tool
def create_product(
    productgroup_id: str,
    fields: list[str] = [],
    params: ProductGroupCreateProductParams | dict = {},
):
    """Create Product for this ProductGroup.

    Args:
        productgroup_id: The ID of the ProductGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductGroupCreateProductParams type.
    """
    return ProductGroup(productgroup_id).create_product(fields=fields, params=params)
