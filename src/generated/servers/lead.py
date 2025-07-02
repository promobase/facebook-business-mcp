"""Lead MCP Server with typed wrappers."""

from facebook_business.adobjects.lead import Lead
from fastmcp import FastMCP

from src.generated.models.lead import LeadField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLead"
instructions = """
Lead MCP Server for Facebook Business API.

Provides typed access to all Lead operations.
"""

lead_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@lead_server.tool
@wrapped_fn_tool
def get_lead(
    lead_id: str,
    fields: list[LeadField] = [],
) -> str:
    """Get a Lead object by ID.

    Args:
        lead_id: The ID of the Lead.
        fields: Fields to retrieve. Available fields: See LeadField type.
    """
    obj = Lead(lead_id)
    return obj.api_get(fields=fields)


@lead_server.tool
@wrapped_fn_tool
def delete_lead(
    lead_id: str,
) -> str:
    """Delete a Lead object.

    Args:
        lead_id: The ID of the Lead.
    """
    return Lead(lead_id).api_delete()
