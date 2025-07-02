"""CPASAdCreationTemplate MCP Server."""

from typing import Any

from facebook_business.adobjects.cpasadcreationtemplate import CPASAdCreationTemplate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASAdCreationTemplate"
instructions = """
CPASAdCreationTemplate MCP Server for Facebook Business API.

Provides typed access to all CPASAdCreationTemplate operations.
"""

cpasadcreationtemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasadcreationtemplate_server.tool
@wrapped_fn_tool
def get_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
) -> str:
    obj = CPASAdCreationTemplate(cpasadcreationtemplate_id)
    return obj.api_get(fields=fields)
