"""WebsiteCreativeAssetSuggestions MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.websitecreativeassetsuggestions import (
    WebsiteCreativeAssetSuggestions,
)
from fastmcp import FastMCP

from src.generated.models.websitecreativeassetsuggestions import (
    WebsiteCreativeAssetSuggestionsField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWebsiteCreativeAssetSuggestions"
instructions = """
WebsiteCreativeAssetSuggestions MCP Server for Facebook Business API.

Provides typed access to all WebsiteCreativeAssetSuggestions operations.
"""

websitecreativeassetsuggestions_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@websitecreativeassetsuggestions_server.tool
@wrapped_fn_tool
def get_websitecreativeassetsuggestions(
    websitecreativeassetsuggestions_id: str,
    fields: list[WebsiteCreativeAssetSuggestionsField] = [],
) -> str:
    """Get a WebsiteCreativeAssetSuggestions object by ID.

    Args:
        websitecreativeassetsuggestions_id: The ID of the WebsiteCreativeAssetSuggestions.
        fields: Fields to retrieve. Available fields: See WebsiteCreativeAssetSuggestionsField type.
    """
    obj = WebsiteCreativeAssetSuggestions(websitecreativeassetsuggestions_id)
    return obj.api_get(fields=fields)
