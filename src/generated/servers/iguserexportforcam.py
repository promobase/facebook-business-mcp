"""IGUserExportForCAM MCP Server."""

from typing import Any

from facebook_business.adobjects.iguserexportforcam import IGUserExportForCAM
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUserExportForCAM"
instructions = """
IGUserExportForCAM MCP Server for Facebook Business API.

Provides typed access to all IGUserExportForCAM operations.
"""

iguserexportforcam_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguserexportforcam_server.tool
@wrapped_fn_tool
def get_iguserexportforcam(
    iguserexportforcam_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGUserExportForCAM(iguserexportforcam_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@iguserexportforcam_server.tool
@wrapped_fn_tool
def get_insights(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserExportForCAM(iguserexportforcam_id).get_insights(fields=fields, params=params)
