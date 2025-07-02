"""ProductItemLocalInfo MCP Server with typed wrappers."""

from facebook_business.adobjects.productitemlocalinfo import ProductItemLocalInfo
from fastmcp import FastMCP

from src.generated.models.productitemlocalinfo import ProductItemLocalInfoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductItemLocalInfo"
instructions = """
ProductItemLocalInfo MCP Server for Facebook Business API.

Provides typed access to all ProductItemLocalInfo operations.
"""

productitemlocalinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productitemlocalinfo_server.tool
@wrapped_fn_tool
def get_productitemlocalinfo(
    productitemlocalinfo_id: str,
    fields: list[ProductItemLocalInfoField] = [],
) -> str:
    """Get a ProductItemLocalInfo object by ID.

    Args:
        productitemlocalinfo_id: The ID of the ProductItemLocalInfo.
        fields: Fields to retrieve. Available fields: See ProductItemLocalInfoField type.
    """
    obj = ProductItemLocalInfo(productitemlocalinfo_id)
    return obj.api_get(fields=fields)
