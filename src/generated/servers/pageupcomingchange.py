"""PageUpcomingChange MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.pageupcomingchange import PageUpcomingChange
from fastmcp import FastMCP

from src.generated.models.pageupcomingchange import PageUpcomingChangeField
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
    fields: list[PageUpcomingChangeField] = [],
) -> str:
    """Get a PageUpcomingChange object by ID.

    Args:
        pageupcomingchange_id: The ID of the PageUpcomingChange.
        fields: Fields to retrieve. Available fields: See PageUpcomingChangeField type.
    """
    obj = PageUpcomingChange(pageupcomingchange_id)
    return obj.api_get(fields=fields)
