"""AdTopline MCP Server."""

from typing import Any

from facebook_business.adobjects.adtopline import AdTopline
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdTopline"
instructions = """
AdTopline MCP Server for Facebook Business API.

Provides typed access to all AdTopline operations.
"""

adtopline_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adtopline_server.tool
@wrapped_fn_tool
def get_adtopline(
    adtopline_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdTopline(adtopline_id)
    return obj.api_get(fields=fields)
