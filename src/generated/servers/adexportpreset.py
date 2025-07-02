"""AdExportPreset MCP Server."""

from typing import Any

from facebook_business.adobjects.adexportpreset import AdExportPreset
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdExportPreset"
instructions = """
AdExportPreset MCP Server for Facebook Business API.

Provides typed access to all AdExportPreset operations.
"""

adexportpreset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adexportpreset_server.tool
@wrapped_fn_tool
def get_adexportpreset(
    adexportpreset_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdExportPreset(adexportpreset_id)
    return obj.api_get(fields=fields)
