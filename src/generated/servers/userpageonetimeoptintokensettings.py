"""UserPageOneTimeOptInTokenSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettings,
)
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = UserPageOneTimeOptInTokenSettings(userpageonetimeoptintokensettings_id)
    return obj.api_get(fields=fields)
