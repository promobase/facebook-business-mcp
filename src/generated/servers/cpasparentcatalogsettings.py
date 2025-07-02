"""CPASParentCatalogSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.cpasparentcatalogsettings import CPASParentCatalogSettings
from fastmcp import FastMCP

from src.generated.models.cpasparentcatalogsettings import CPASParentCatalogSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASParentCatalogSettings"
instructions = """
CPASParentCatalogSettings MCP Server for Facebook Business API.

Provides typed access to all CPASParentCatalogSettings operations.
"""

cpasparentcatalogsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasparentcatalogsettings_server.tool
@wrapped_fn_tool
def get_cpasparentcatalogsettings(
    cpasparentcatalogsettings_id: str,
    fields: list[CPASParentCatalogSettingsField] = [],
) -> str:
    """Get a CPASParentCatalogSettings object by ID.

    Args:
        cpasparentcatalogsettings_id: The ID of the CPASParentCatalogSettings.
        fields: Fields to retrieve. Available fields: See CPASParentCatalogSettingsField type.
    """
    obj = CPASParentCatalogSettings(cpasparentcatalogsettings_id)
    return obj.api_get(fields=fields)
