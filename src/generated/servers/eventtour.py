"""EventTour MCP Server with typed wrappers."""

from facebook_business.adobjects.eventtour import EventTour
from fastmcp import FastMCP

from src.generated.models.eventtour import EventTourField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventTour"
instructions = """
EventTour MCP Server for Facebook Business API.

Provides typed access to all EventTour operations.
"""

eventtour_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventtour_server.tool
@wrapped_fn_tool
def get_eventtour(
    eventtour_id: str,
    fields: list[EventTourField] = [],
) -> str:
    """Get a EventTour object by ID.

    Args:
        eventtour_id: The ID of the EventTour.
        fields: Fields to retrieve. Available fields: See EventTourField type.
    """
    obj = EventTour(eventtour_id)
    return obj.api_get(fields=fields)
