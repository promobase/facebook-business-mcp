"""FranchiseProgramMember MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.franchiseprogrammember import FranchiseProgramMember
from fastmcp import FastMCP

from src.generated.models.franchiseprogrammember import FranchiseProgramMemberField
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
    fields: list[FranchiseProgramMemberField] = [],
) -> str:
    """Get a FranchiseProgramMember object by ID.

    Args:
        franchiseprogrammember_id: The ID of the FranchiseProgramMember.
        fields: Fields to retrieve. Available fields: See FranchiseProgramMemberField type.
    """
    obj = FranchiseProgramMember(franchiseprogrammember_id)
    return obj.api_get(fields=fields)
