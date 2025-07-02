"""LeadGenDataDraft MCP Server with typed wrappers."""

from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
from fastmcp import FastMCP

from src.generated.models.leadgendatadraft import LeadGenDataDraftField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLeadGenDataDraft"
instructions = """
LeadGenDataDraft MCP Server for Facebook Business API.

Provides typed access to all LeadGenDataDraft operations.
"""

leadgendatadraft_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@leadgendatadraft_server.tool
@wrapped_fn_tool
def get_leadgendatadraft(
    leadgendatadraft_id: str,
    fields: list[LeadGenDataDraftField] = [],
) -> str:
    """Get a LeadGenDataDraft object by ID.

    Args:
        leadgendatadraft_id: The ID of the LeadGenDataDraft.
        fields: Fields to retrieve. Available fields: See LeadGenDataDraftField type.
    """
    obj = LeadGenDataDraft(leadgendatadraft_id)
    return obj.api_get(fields=fields)
