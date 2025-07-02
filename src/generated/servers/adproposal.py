"""AdProposal MCP Server with typed wrappers."""

from facebook_business.adobjects.adproposal import AdProposal
from fastmcp import FastMCP

from src.generated.models.adproposal import AdProposalField
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
    fields: list[AdProposalField] = [],
) -> str:
    """Get a AdProposal object by ID.

    Args:
        adproposal_id: The ID of the AdProposal.
        fields: Fields to retrieve. Available fields: See AdProposalField type.
    """
    obj = AdProposal(adproposal_id)
    return obj.api_get(fields=fields)
