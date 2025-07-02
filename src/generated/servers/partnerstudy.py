"""PartnerStudy MCP Server."""

from typing import Any

from facebook_business.adobjects.partnerstudy import PartnerStudy
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPartnerStudy"
instructions = """
PartnerStudy MCP Server for Facebook Business API.

Provides typed access to all PartnerStudy operations.
"""

partnerstudy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@partnerstudy_server.tool
@wrapped_fn_tool
def get_partnerstudy(
    partnerstudy_id: str,
    fields: list[str] = [],
) -> str:
    obj = PartnerStudy(partnerstudy_id)
    return obj.api_get(fields=fields)
