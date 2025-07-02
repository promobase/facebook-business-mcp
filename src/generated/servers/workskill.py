"""WorkSkill MCP Server."""

from typing import Any

from facebook_business.adobjects.workskill import WorkSkill
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWorkSkill"
instructions = """
WorkSkill MCP Server for Facebook Business API.

Provides typed access to all WorkSkill operations.
"""

workskill_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@workskill_server.tool
@wrapped_fn_tool
def get_workskill(
    workskill_id: str,
    fields: list[str] = [],
) -> str:
    obj = WorkSkill(workskill_id)
    return obj.api_get(fields=fields)
