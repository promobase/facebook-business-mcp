"""AdProposal MCP Server."""

from typing import Any

from facebook_business.adobjects.adproposal import AdProposal
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdProposal"
instructions = """
AdProposal MCP Server for Facebook Business API.

Provides typed access to all AdProposal operations.
"""

adproposal_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adproposal_server.tool
@wrapped_fn_tool
def get_adproposal(
    adproposal_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdProposal(adproposal_id)
    return obj.api_get(fields=fields)
