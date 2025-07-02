"""ManagementSiteLink MCP Server with typed wrappers."""

from facebook_business.adobjects.managementsitelink import ManagementSiteLink
from fastmcp import FastMCP

from src.generated.models.managementsitelink import ManagementSiteLinkField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookManagementSiteLink"
instructions = """
ManagementSiteLink MCP Server for Facebook Business API.

Provides typed access to all ManagementSiteLink operations.
"""

managementsitelink_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@managementsitelink_server.tool
@wrapped_fn_tool
def get_managementsitelink(
    managementsitelink_id: str,
    fields: list[ManagementSiteLinkField] = [],
) -> str:
    """Get a ManagementSiteLink object by ID.

    Args:
        managementsitelink_id: The ID of the ManagementSiteLink.
        fields: Fields to retrieve. Available fields: See ManagementSiteLinkField type.
    """
    obj = ManagementSiteLink(managementsitelink_id)
    return obj.api_get(fields=fields)
