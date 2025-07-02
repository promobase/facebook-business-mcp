"""ALMEvent MCP Server with typed wrappers."""

from facebook_business.adobjects.almevent import ALMEvent
from fastmcp import FastMCP

from src.generated.models.almevent import ALMEventField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMEvent"
instructions = """
ALMEvent MCP Server for Facebook Business API.

Provides typed access to all ALMEvent operations.
"""

almevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almevent_server.tool
@wrapped_fn_tool
def get_almevent(
    almevent_id: str,
    fields: list[ALMEventField] = [],
) -> str:
    """Get a ALMEvent object by ID.

    Args:
        almevent_id: The ID of the ALMEvent.
        fields: Fields to retrieve. Available fields: See ALMEventField type.
    """
    obj = ALMEvent(almevent_id)
    return obj.api_get(fields=fields)
