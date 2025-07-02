"""ProductSetUsage MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productsetusage import ProductSetUsage
from fastmcp import FastMCP

from src.generated.models.productsetusage import ProductSetUsageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductSetUsage"
instructions = """
ProductSetUsage MCP Server for Facebook Business API.

Provides typed access to all ProductSetUsage operations.
"""

productsetusage_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productsetusage_server.tool
@wrapped_fn_tool
def get_productsetusage(
    productsetusage_id: str,
    fields: list[ProductSetUsageField] = [],
) -> str:
    """Get a ProductSetUsage object by ID.

    Args:
        productsetusage_id: The ID of the ProductSetUsage.
        fields: Fields to retrieve. Available fields: See ProductSetUsageField type.
    """
    obj = ProductSetUsage(productsetusage_id)
    return obj.api_get(fields=fields)
