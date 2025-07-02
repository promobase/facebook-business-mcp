"""EventExternalTicketInfo MCP Server with typed wrappers."""

from facebook_business.adobjects.eventexternalticketinfo import EventExternalTicketInfo
from fastmcp import FastMCP

from src.generated.models.eventexternalticketinfo import EventExternalTicketInfoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventExternalTicketInfo"
instructions = """
EventExternalTicketInfo MCP Server for Facebook Business API.

Provides typed access to all EventExternalTicketInfo operations.
"""

eventexternalticketinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventexternalticketinfo_server.tool
@wrapped_fn_tool
def get_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    fields: list[EventExternalTicketInfoField] = [],
) -> str:
    """Get a EventExternalTicketInfo object by ID.

    Args:
        eventexternalticketinfo_id: The ID of the EventExternalTicketInfo.
        fields: Fields to retrieve. Available fields: See EventExternalTicketInfoField type.
    """
    obj = EventExternalTicketInfo(eventexternalticketinfo_id)
    return obj.api_get(fields=fields)
