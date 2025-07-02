"""BrandSafetyDownloadable MCP Server."""

from typing import Any

from facebook_business.adobjects.brandsafetydownloadable import BrandSafetyDownloadable
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBrandSafetyDownloadable"
instructions = """
BrandSafetyDownloadable MCP Server for Facebook Business API.

Provides typed access to all BrandSafetyDownloadable operations.
"""

brandsafetydownloadable_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@brandsafetydownloadable_server.tool
@wrapped_fn_tool
def get_brandsafetydownloadable(
    brandsafetydownloadable_id: str,
    fields: list[str] = [],
) -> str:
    obj = BrandSafetyDownloadable(brandsafetydownloadable_id)
    return obj.api_get(fields=fields)
