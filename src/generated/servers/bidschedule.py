"""BidSchedule MCP Server with typed wrappers."""

from facebook_business.adobjects.bidschedule import BidSchedule
from fastmcp import FastMCP

from src.generated.models.bidschedule import BidScheduleField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBidSchedule"
instructions = """
BidSchedule MCP Server for Facebook Business API.

Provides typed access to all BidSchedule operations.
"""

bidschedule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@bidschedule_server.tool
@wrapped_fn_tool
def get_bidschedule(
    bidschedule_id: str,
    fields: list[BidScheduleField] = [],
) -> str:
    """Get a BidSchedule object by ID.

    Args:
        bidschedule_id: The ID of the BidSchedule.
        fields: Fields to retrieve. Available fields: See BidScheduleField type.
    """
    obj = BidSchedule(bidschedule_id)
    return obj.api_get(fields=fields)
