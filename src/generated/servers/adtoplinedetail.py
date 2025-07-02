"""AdToplineDetail MCP Server."""

from typing import Any

from facebook_business.adobjects.adtoplinedetail import AdToplineDetail
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdToplineDetail"
instructions = """
AdToplineDetail MCP Server for Facebook Business API.

Provides typed access to all AdToplineDetail operations.
"""

adtoplinedetail_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adtoplinedetail_server.tool
@wrapped_fn_tool
def get_adtoplinedetail(
    adtoplinedetail_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdToplineDetail(adtoplinedetail_id)
    return obj.api_get(fields=fields)
