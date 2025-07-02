"""ProductCatalogCategory MCP Server."""

from typing import Any

from facebook_business.adobjects.productcatalogcategory import ProductCatalogCategory
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductCatalogCategory"
instructions = """
ProductCatalogCategory MCP Server for Facebook Business API.

Provides typed access to all ProductCatalogCategory operations.
"""

productcatalogcategory_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@productcatalogcategory_server.tool
@wrapped_fn_tool
def get_endpoint(
    productcatalogcategory_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalogCategory(productcatalogcategory_id).get_endpoint(
        fields=fields, params=params
    )
