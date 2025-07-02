"""OpenGraphContext MCP Server."""

from typing import Any

from facebook_business.adobjects.opengraphcontext import OpenGraphContext
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOpenGraphContext"
instructions = """
OpenGraphContext MCP Server for Facebook Business API.

Provides typed access to all OpenGraphContext operations.
"""

opengraphcontext_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@opengraphcontext_server.tool
@wrapped_fn_tool
def get_opengraphcontext(
    opengraphcontext_id: str,
    fields: list[str] = [],
) -> str:
    obj = OpenGraphContext(opengraphcontext_id)
    return obj.api_get(fields=fields)
