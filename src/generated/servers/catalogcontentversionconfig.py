"""CatalogContentVersionConfig MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.catalogcontentversionconfig import CatalogContentVersionConfig
from fastmcp import FastMCP

from src.generated.models.catalogcontentversionconfig import CatalogContentVersionConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogContentVersionConfig"
instructions = """
CatalogContentVersionConfig MCP Server for Facebook Business API.

Provides typed access to all CatalogContentVersionConfig operations.
"""

catalogcontentversionconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogcontentversionconfig_server.tool
@wrapped_fn_tool
def get_catalogcontentversionconfig(
    catalogcontentversionconfig_id: str,
    fields: list[CatalogContentVersionConfigField] = [],
) -> str:
    """Get a CatalogContentVersionConfig object by ID.

    Args:
        catalogcontentversionconfig_id: The ID of the CatalogContentVersionConfig.
        fields: Fields to retrieve. Available fields: See CatalogContentVersionConfigField type.
    """
    obj = CatalogContentVersionConfig(catalogcontentversionconfig_id)
    return obj.api_get(fields=fields)
