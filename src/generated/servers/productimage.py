"""ProductImage MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productimage import ProductImage
from fastmcp import FastMCP

from src.generated.models.productimage import ProductImageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductImage"
instructions = """
ProductImage MCP Server for Facebook Business API.

Provides typed access to all ProductImage operations.
"""

productimage_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productimage_server.tool
@wrapped_fn_tool
def get_productimage(
    productimage_id: str,
    fields: list[ProductImageField] = [],
) -> str:
    """Get a ProductImage object by ID.

    Args:
        productimage_id: The ID of the ProductImage.
        fields: Fields to retrieve. Available fields: See ProductImageField type.
    """
    obj = ProductImage(productimage_id)
    return obj.api_get(fields=fields)
