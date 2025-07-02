"""AdStudyCell MCP Server."""

from typing import Any

from facebook_business.adobjects.adstudycell import AdStudyCell
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudyCell"
instructions = """
AdStudyCell MCP Server for Facebook Business API.

Provides typed access to all AdStudyCell operations.
"""

adstudycell_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adstudycell_server.tool
@wrapped_fn_tool
def get_adstudycell(
    adstudycell_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdStudyCell(adstudycell_id)
    return obj.api_get(fields=fields)


@adstudycell_server.tool
@wrapped_fn_tool
def update_adstudycell(
    adstudycell_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdStudyCell(adstudycell_id).api_update(fields=fields, params=params)
