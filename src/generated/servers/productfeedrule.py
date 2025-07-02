"""ProductFeedRule MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productfeedrule import ProductFeedRule
from fastmcp import FastMCP

from src.generated.models.productfeedrule import ProductFeedRuleField, ProductFeedRuleUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeedRule"
instructions = """
ProductFeedRule MCP Server for Facebook Business API.

Provides typed access to all ProductFeedRule operations.
"""

productfeedrule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productfeedrule_server.tool
@wrapped_fn_tool
def get_productfeedrule(
    productfeedrule_id: str,
    fields: list[ProductFeedRuleField] = [],
) -> str:
    """Get a ProductFeedRule object by ID.

    Args:
        productfeedrule_id: The ID of the ProductFeedRule.
        fields: Fields to retrieve. Available fields: See ProductFeedRuleField type.
    """
    obj = ProductFeedRule(productfeedrule_id)
    return obj.api_get(fields=fields)


@productfeedrule_server.tool
@wrapped_fn_tool
def update_productfeedrule(
    productfeedrule_id: str,
    fields: list[ProductFeedRuleField] = [],
    params: ProductFeedRuleUpdateParams | dict = {},
) -> str:
    """Update a ProductFeedRule object.

    Args:
        productfeedrule_id: The ID of the ProductFeedRule.
        fields: Fields to return after update. Available fields: See ProductFeedRuleField type.
        params: Parameters to update. Available params: See ProductFeedRuleUpdateParams type.
    """
    return ProductFeedRule(productfeedrule_id).api_update(fields=fields, params=params)


@productfeedrule_server.tool
@wrapped_fn_tool
def delete_productfeedrule(
    productfeedrule_id: str,
) -> str:
    """Delete a ProductFeedRule object.

    Args:
        productfeedrule_id: The ID of the ProductFeedRule.
    """
    return ProductFeedRule(productfeedrule_id).api_delete()
