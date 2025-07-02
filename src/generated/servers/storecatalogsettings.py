"""StoreCatalogSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.storecatalogsettings import StoreCatalogSettings
from fastmcp import FastMCP

from src.generated.models.storecatalogsettings import StoreCatalogSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookStoreCatalogSettings"
instructions = """
StoreCatalogSettings MCP Server for Facebook Business API.

Provides typed access to all StoreCatalogSettings operations.
"""

storecatalogsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@storecatalogsettings_server.tool
@wrapped_fn_tool
def get_storecatalogsettings(
    storecatalogsettings_id: str,
    fields: list[StoreCatalogSettingsField] = [],
) -> str:
    """Get a StoreCatalogSettings object by ID.

    Args:
        storecatalogsettings_id: The ID of the StoreCatalogSettings.
        fields: Fields to retrieve. Available fields: See StoreCatalogSettingsField type.
    """
    obj = StoreCatalogSettings(storecatalogsettings_id)
    return obj.api_get(fields=fields)


@storecatalogsettings_server.tool
@wrapped_fn_tool
def delete_storecatalogsettings(
    storecatalogsettings_id: str,
) -> str:
    """Delete a StoreCatalogSettings object.

    Args:
        storecatalogsettings_id: The ID of the StoreCatalogSettings.
    """
    return StoreCatalogSettings(storecatalogsettings_id).api_delete()
