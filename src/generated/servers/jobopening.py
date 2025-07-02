"""JobOpening MCP Server."""

from typing import Any

from facebook_business.adobjects.jobopening import JobOpening
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookJobOpening"
instructions = """
JobOpening MCP Server for Facebook Business API.

Provides typed access to all JobOpening operations.
"""

jobopening_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@jobopening_server.tool
@wrapped_fn_tool
def get_jobopening(
    jobopening_id: str,
    fields: list[str] = [],
) -> str:
    obj = JobOpening(jobopening_id)
    return obj.api_get(fields=fields)
