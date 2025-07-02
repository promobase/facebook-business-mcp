"""ProductCatalogLocalizationSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.productcataloglocalizationsettings import (
    ProductCatalogLocalizationSettings,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductCatalogLocalizationSettings"
instructions = """
ProductCatalogLocalizationSettings MCP Server for Facebook Business API.

Provides typed access to all ProductCatalogLocalizationSettings operations.
"""

productcataloglocalizationsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@productcataloglocalizationsettings_server.tool
@wrapped_fn_tool
def get_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductCatalogLocalizationSettings(productcataloglocalizationsettings_id)
    return obj.api_get(fields=fields)
