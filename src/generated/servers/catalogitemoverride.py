"""CatalogItemOverride MCP Server with typed wrappers."""

from facebook_business.adobjects.catalogitemoverride import CatalogItemOverride
from fastmcp import FastMCP

from src.generated.models.catalogitemoverride import CatalogItemOverrideField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogItemOverride"
instructions = """
CatalogItemOverride MCP Server for Facebook Business API.

Provides typed access to all CatalogItemOverride operations.
"""

catalogitemoverride_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogitemoverride_server.tool
@wrapped_fn_tool
def get_catalogitemoverride(
    catalogitemoverride_id: str,
    fields: list[CatalogItemOverrideField] = [],
) -> str:
    """Get a CatalogItemOverride object by ID.

    Args:
        catalogitemoverride_id: The ID of the CatalogItemOverride.
        fields: Fields to retrieve. Available fields: See CatalogItemOverrideField type.
    """
    obj = CatalogItemOverride(catalogitemoverride_id)
    return obj.api_get(fields=fields)
