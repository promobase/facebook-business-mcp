"""Shop MCP Server."""

from typing import Any

from facebook_business.adobjects.shop import Shop
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookShop"
instructions = """
Shop MCP Server for Facebook Business API.

Provides typed access to all Shop operations.
"""

shop_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@shop_server.tool
@wrapped_fn_tool
def get_shop(
    shop_id: str,
    fields: list[str] = [],
) -> str:
    obj = Shop(shop_id)
    return obj.api_get(fields=fields)
