"""FAMEKumo MCP Server."""

from typing import Any

from facebook_business.adobjects.famekumo import FAMEKumo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFAMEKumo"
instructions = """
FAMEKumo MCP Server for Facebook Business API.

Provides typed access to all FAMEKumo operations.
"""

famekumo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@famekumo_server.tool
@wrapped_fn_tool
def get_famekumo(
    famekumo_id: str,
    fields: list[str] = [],
) -> str:
    obj = FAMEKumo(famekumo_id)
    return obj.api_get(fields=fields)
