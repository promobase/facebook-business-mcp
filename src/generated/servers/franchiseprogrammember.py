"""FranchiseProgramMember MCP Server."""

from typing import Any

from facebook_business.adobjects.franchiseprogrammember import FranchiseProgramMember
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFranchiseProgramMember"
instructions = """
FranchiseProgramMember MCP Server for Facebook Business API.

Provides typed access to all FranchiseProgramMember operations.
"""

franchiseprogrammember_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@franchiseprogrammember_server.tool
@wrapped_fn_tool
def get_franchiseprogrammember(
    franchiseprogrammember_id: str,
    fields: list[str] = [],
) -> str:
    obj = FranchiseProgramMember(franchiseprogrammember_id)
    return obj.api_get(fields=fields)
