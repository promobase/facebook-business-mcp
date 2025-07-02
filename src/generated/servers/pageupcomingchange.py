"""PageUpcomingChange MCP Server."""

from typing import Any

from facebook_business.adobjects.pageupcomingchange import PageUpcomingChange
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageUpcomingChange"
instructions = """
PageUpcomingChange MCP Server for Facebook Business API.

Provides typed access to all PageUpcomingChange operations.
"""

pageupcomingchange_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pageupcomingchange_server.tool
@wrapped_fn_tool
def get_pageupcomingchange(
    pageupcomingchange_id: str,
    fields: list[str] = [],
) -> str:
    obj = PageUpcomingChange(pageupcomingchange_id)
    return obj.api_get(fields=fields)
