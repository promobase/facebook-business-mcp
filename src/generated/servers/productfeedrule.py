"""ProductFeedRule MCP Server."""

from typing import Any

from facebook_business.adobjects.productfeedrule import ProductFeedRule
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ProductFeedRule(productfeedrule_id)
    return obj.api_get(fields=fields)


@productfeedrule_server.tool
@wrapped_fn_tool
def update_productfeedrule(
    productfeedrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductFeedRule(productfeedrule_id).api_update(fields=fields, params=params)


@productfeedrule_server.tool
@wrapped_fn_tool
def delete_productfeedrule(
    productfeedrule_id: str,
) -> str:
    return ProductFeedRule(productfeedrule_id).api_delete()
