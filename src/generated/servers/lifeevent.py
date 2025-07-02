"""LifeEvent MCP Server with typed wrappers."""

from facebook_business.adobjects.lifeevent import LifeEvent
from fastmcp import FastMCP

from src.generated.models.lifeevent import LifeEventField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLifeEvent"
instructions = """
LifeEvent MCP Server for Facebook Business API.

Provides typed access to all LifeEvent operations.
"""

lifeevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@lifeevent_server.tool
@wrapped_fn_tool
def get_lifeevent(
    lifeevent_id: str,
    fields: list[LifeEventField] = [],
) -> str:
    """Get a LifeEvent object by ID.

    Args:
        lifeevent_id: The ID of the LifeEvent.
        fields: Fields to retrieve. Available fields: See LifeEventField type.
    """
    obj = LifeEvent(lifeevent_id)
    return obj.api_get(fields=fields)
