"""AdvAInstance MCP Server."""

from typing import Any

from facebook_business.adobjects.advainstance import AdvAInstance
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdvAInstance"
instructions = """
AdvAInstance MCP Server for Facebook Business API.

Provides typed access to all AdvAInstance operations.
"""

advainstance_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@advainstance_server.tool
@wrapped_fn_tool
def get_advainstance(
    advainstance_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdvAInstance(advainstance_id)
    return obj.api_get(fields=fields)
