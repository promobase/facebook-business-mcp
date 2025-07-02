"""PageBroadcast MCP Server with typed wrappers."""

from facebook_business.adobjects.pagebroadcast import PageBroadcast
from fastmcp import FastMCP

from src.generated.models.pagebroadcast import PageBroadcastField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageBroadcast"
instructions = """
PageBroadcast MCP Server for Facebook Business API.

Provides typed access to all PageBroadcast operations.
"""

pagebroadcast_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pagebroadcast_server.tool
@wrapped_fn_tool
def get_pagebroadcast(
    pagebroadcast_id: str,
    fields: list[PageBroadcastField] = [],
) -> str:
    """Get a PageBroadcast object by ID.

    Args:
        pagebroadcast_id: The ID of the PageBroadcast.
        fields: Fields to retrieve. Available fields: See PageBroadcastField type.
    """
    obj = PageBroadcast(pagebroadcast_id)
    return obj.api_get(fields=fields)
