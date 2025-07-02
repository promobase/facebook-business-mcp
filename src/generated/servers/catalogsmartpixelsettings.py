"""CatalogSmartPixelSettings MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.catalogsmartpixelsettings import CatalogSmartPixelSettings
from fastmcp import FastMCP

from src.generated.models.catalogsmartpixelsettings import CatalogSmartPixelSettingsField
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
    fields: list[CatalogSmartPixelSettingsField] = [],
) -> str:
    """Get a CatalogSmartPixelSettings object by ID.

    Args:
        catalogsmartpixelsettings_id: The ID of the CatalogSmartPixelSettings.
        fields: Fields to retrieve. Available fields: See CatalogSmartPixelSettingsField type.
    """
    obj = CatalogSmartPixelSettings(catalogsmartpixelsettings_id)
    return obj.api_get(fields=fields)
