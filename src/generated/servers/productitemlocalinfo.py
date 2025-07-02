"""ProductItemLocalInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.productitemlocalinfo import ProductItemLocalInfo
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ProductItemLocalInfo(productitemlocalinfo_id)
    return obj.api_get(fields=fields)
