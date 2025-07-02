"""IGUpcomingEvent MCP Server with typed wrappers."""

from facebook_business.adobjects.igupcomingevent import IGUpcomingEvent
from fastmcp import FastMCP

from src.generated.models.igupcomingevent import IGUpcomingEventField, IGUpcomingEventUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUpcomingEvent"
instructions = """
IGUpcomingEvent MCP Server for Facebook Business API.

Provides typed access to all IGUpcomingEvent operations.
"""

igupcomingevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igupcomingevent_server.tool
@wrapped_fn_tool
def get_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[IGUpcomingEventField] = [],
) -> str:
    """Get a IGUpcomingEvent object by ID.

    Args:
        igupcomingevent_id: The ID of the IGUpcomingEvent.
        fields: Fields to retrieve. Available fields: See IGUpcomingEventField type.
    """
    obj = IGUpcomingEvent(igupcomingevent_id)
    return obj.api_get(fields=fields)


@igupcomingevent_server.tool
@wrapped_fn_tool
def update_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[IGUpcomingEventField] = [],
    params: IGUpcomingEventUpdateParams | dict = {},
) -> str:
    """Update a IGUpcomingEvent object.

    Args:
        igupcomingevent_id: The ID of the IGUpcomingEvent.
        fields: Fields to return after update. Available fields: See IGUpcomingEventField type.
        params: Parameters to update. Available params: See IGUpcomingEventUpdateParams type.
    """
    return IGUpcomingEvent(igupcomingevent_id).api_update(fields=fields, params=params)
