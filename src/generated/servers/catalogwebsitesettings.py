"""CatalogWebsiteSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.catalogwebsitesettings import CatalogWebsiteSettings
from fastmcp import FastMCP

from src.generated.models.catalogwebsitesettings import CatalogWebsiteSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogWebsiteSettings"
instructions = """
CatalogWebsiteSettings MCP Server for Facebook Business API.

Provides typed access to all CatalogWebsiteSettings operations.
"""

catalogwebsitesettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogwebsitesettings_server.tool
@wrapped_fn_tool
def get_catalogwebsitesettings(
    catalogwebsitesettings_id: str,
    fields: list[CatalogWebsiteSettingsField] = [],
) -> str:
    """Get a CatalogWebsiteSettings object by ID.

    Args:
        catalogwebsitesettings_id: The ID of the CatalogWebsiteSettings.
        fields: Fields to retrieve. Available fields: See CatalogWebsiteSettingsField type.
    """
    obj = CatalogWebsiteSettings(catalogwebsitesettings_id)
    return obj.api_get(fields=fields)
