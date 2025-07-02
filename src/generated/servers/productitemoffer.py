"""ProductItemOffer MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productitemoffer import ProductItemOffer
from fastmcp import FastMCP

from src.generated.models.productitemoffer import ProductItemOfferField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductItemOffer"
instructions = """
ProductItemOffer MCP Server for Facebook Business API.

Provides typed access to all ProductItemOffer operations.
"""

productitemoffer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productitemoffer_server.tool
@wrapped_fn_tool
def get_productitemoffer(
    productitemoffer_id: str,
    fields: list[ProductItemOfferField] = [],
) -> str:
    """Get a ProductItemOffer object by ID.

    Args:
        productitemoffer_id: The ID of the ProductItemOffer.
        fields: Fields to retrieve. Available fields: See ProductItemOfferField type.
    """
    obj = ProductItemOffer(productitemoffer_id)
    return obj.api_get(fields=fields)
