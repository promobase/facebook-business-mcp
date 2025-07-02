"""CatalogSmartPixelSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.catalogsmartpixelsettings import CatalogSmartPixelSettings
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogSmartPixelSettings"
instructions = """
CatalogSmartPixelSettings MCP Server for Facebook Business API.

Provides typed access to all CatalogSmartPixelSettings operations.
"""

catalogsmartpixelsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogsmartpixelsettings_server.tool
@wrapped_fn_tool
def get_catalogsmartpixelsettings(
    catalogsmartpixelsettings_id: str,
    fields: list[str] = [],
) -> str:
    obj = CatalogSmartPixelSettings(catalogsmartpixelsettings_id)
    return obj.api_get(fields=fields)
