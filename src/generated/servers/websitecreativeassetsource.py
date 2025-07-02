"""WebsiteCreativeAssetSource MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.websitecreativeassetsource import WebsiteCreativeAssetSource
from fastmcp import FastMCP

from src.generated.models.websitecreativeassetsource import WebsiteCreativeAssetSourceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWebsiteCreativeAssetSource"
instructions = """
WebsiteCreativeAssetSource MCP Server for Facebook Business API.

Provides typed access to all WebsiteCreativeAssetSource operations.
"""

websitecreativeassetsource_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@websitecreativeassetsource_server.tool
@wrapped_fn_tool
def get_websitecreativeassetsource(
    websitecreativeassetsource_id: str,
    fields: list[WebsiteCreativeAssetSourceField] = [],
) -> str:
    """Get a WebsiteCreativeAssetSource object by ID.

    Args:
        websitecreativeassetsource_id: The ID of the WebsiteCreativeAssetSource.
        fields: Fields to retrieve. Available fields: See WebsiteCreativeAssetSourceField type.
    """
    obj = WebsiteCreativeAssetSource(websitecreativeassetsource_id)
    return obj.api_get(fields=fields)
