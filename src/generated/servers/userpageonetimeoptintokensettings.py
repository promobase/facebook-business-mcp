"""UserPageOneTimeOptInTokenSettings MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettings,
)
from fastmcp import FastMCP

from src.generated.models.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettingsField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookUserPageOneTimeOptInTokenSettings"
instructions = """
UserPageOneTimeOptInTokenSettings MCP Server for Facebook Business API.

Provides typed access to all UserPageOneTimeOptInTokenSettings operations.
"""

userpageonetimeoptintokensettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@userpageonetimeoptintokensettings_server.tool
@wrapped_fn_tool
def get_userpageonetimeoptintokensettings(
    userpageonetimeoptintokensettings_id: str,
    fields: list[UserPageOneTimeOptInTokenSettingsField] = [],
) -> str:
    """Get a UserPageOneTimeOptInTokenSettings object by ID.

    Args:
        userpageonetimeoptintokensettings_id: The ID of the UserPageOneTimeOptInTokenSettings.
        fields: Fields to retrieve. Available fields: See UserPageOneTimeOptInTokenSettingsField type.
    """
    obj = UserPageOneTimeOptInTokenSettings(userpageonetimeoptintokensettings_id)
    return obj.api_get(fields=fields)
