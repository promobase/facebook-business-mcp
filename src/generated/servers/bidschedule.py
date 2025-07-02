"""BidSchedule MCP Server."""

from typing import Any

from facebook_business.adobjects.bidschedule import BidSchedule
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = BidSchedule(bidschedule_id)
    return obj.api_get(fields=fields)
