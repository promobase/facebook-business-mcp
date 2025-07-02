"""SiteLink MCP Server with typed wrappers."""

from facebook_business.adobjects.sitelink import SiteLink
from fastmcp import FastMCP

from src.generated.models.sitelink import SiteLinkField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSiteLink"
instructions = """
SiteLink MCP Server for Facebook Business API.

Provides typed access to all SiteLink operations.
"""

sitelink_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@sitelink_server.tool
@wrapped_fn_tool
def get_sitelink(
    sitelink_id: str,
    fields: list[SiteLinkField] = [],
) -> str:
    """Get a SiteLink object by ID.

    Args:
        sitelink_id: The ID of the SiteLink.
        fields: Fields to retrieve. Available fields: See SiteLinkField type.
    """
    obj = SiteLink(sitelink_id)
    return obj.api_get(fields=fields)
