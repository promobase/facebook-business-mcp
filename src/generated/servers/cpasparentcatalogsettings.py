"""CPASParentCatalogSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.cpasparentcatalogsettings import CPASParentCatalogSettings
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = CPASParentCatalogSettings(cpasparentcatalogsettings_id)
    return obj.api_get(fields=fields)
