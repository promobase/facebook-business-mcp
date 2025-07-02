"""ProductItemOffer MCP Server."""

from typing import Any

from facebook_business.adobjects.productitemoffer import ProductItemOffer
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ProductItemOffer(productitemoffer_id)
    return obj.api_get(fields=fields)
