"""CollaborativeAdsShareSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.collaborativeadssharesettings import CollaborativeAdsShareSettings
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = CollaborativeAdsShareSettings(collaborativeadssharesettings_id)
    return obj.api_get(fields=fields)
