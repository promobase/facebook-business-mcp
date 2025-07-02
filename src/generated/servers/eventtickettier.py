"""EventTicketTier MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.eventtickettier import EventTicketTier
from fastmcp import FastMCP

from src.generated.models.eventtickettier import EventTicketTierField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventTicketTier"
instructions = """
EventTicketTier MCP Server for Facebook Business API.

Provides typed access to all EventTicketTier operations.
"""

eventtickettier_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventtickettier_server.tool
@wrapped_fn_tool
def get_eventtickettier(
    eventtickettier_id: str,
    fields: list[EventTicketTierField] = [],
) -> str:
    """Get a EventTicketTier object by ID.

    Args:
        eventtickettier_id: The ID of the EventTicketTier.
        fields: Fields to retrieve. Available fields: See EventTicketTierField type.
    """
    obj = EventTicketTier(eventtickettier_id)
    return obj.api_get(fields=fields)
