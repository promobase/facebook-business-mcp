"""CollaborativeAdsShareSettings MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.collaborativeadssharesettings import CollaborativeAdsShareSettings
from fastmcp import FastMCP

from src.generated.models.collaborativeadssharesettings import CollaborativeAdsShareSettingsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCollaborativeAdsShareSettings"
instructions = """
CollaborativeAdsShareSettings MCP Server for Facebook Business API.

Provides typed access to all CollaborativeAdsShareSettings operations.
"""

collaborativeadssharesettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@collaborativeadssharesettings_server.tool
@wrapped_fn_tool
def get_collaborativeadssharesettings(
    collaborativeadssharesettings_id: str,
    fields: list[CollaborativeAdsShareSettingsField] = [],
) -> str:
    """Get a CollaborativeAdsShareSettings object by ID.

    Args:
        collaborativeadssharesettings_id: The ID of the CollaborativeAdsShareSettings.
        fields: Fields to retrieve. Available fields: See CollaborativeAdsShareSettingsField type.
    """
    obj = CollaborativeAdsShareSettings(collaborativeadssharesettings_id)
    return obj.api_get(fields=fields)
