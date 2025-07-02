"""CatalogWebsiteOnboardingSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.catalogwebsiteonboardingsettings import (
    CatalogWebsiteOnboardingSettings,
)
from fastmcp import FastMCP

from src.generated.models.catalogwebsiteonboardingsettings import (
    CatalogWebsiteOnboardingSettingsField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogWebsiteOnboardingSettings"
instructions = """
CatalogWebsiteOnboardingSettings MCP Server for Facebook Business API.

Provides typed access to all CatalogWebsiteOnboardingSettings operations.
"""

catalogwebsiteonboardingsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogwebsiteonboardingsettings_server.tool
@wrapped_fn_tool
def get_catalogwebsiteonboardingsettings(
    catalogwebsiteonboardingsettings_id: str,
    fields: list[CatalogWebsiteOnboardingSettingsField] = [],
) -> str:
    """Get a CatalogWebsiteOnboardingSettings object by ID.

    Args:
        catalogwebsiteonboardingsettings_id: The ID of the CatalogWebsiteOnboardingSettings.
        fields: Fields to retrieve. Available fields: See CatalogWebsiteOnboardingSettingsField type.
    """
    obj = CatalogWebsiteOnboardingSettings(catalogwebsiteonboardingsettings_id)
    return obj.api_get(fields=fields)
