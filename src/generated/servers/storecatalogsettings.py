"""StoreCatalogSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.storecatalogsettings import StoreCatalogSettings
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = StoreCatalogSettings(storecatalogsettings_id)
    return obj.api_get(fields=fields)


@storecatalogsettings_server.tool
@wrapped_fn_tool
def delete_storecatalogsettings(
    storecatalogsettings_id: str,
) -> str:
    return StoreCatalogSettings(storecatalogsettings_id).api_delete()
