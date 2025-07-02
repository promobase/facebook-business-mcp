"""MessengerBusinessTemplate MCP Server."""

from typing import Any

from facebook_business.adobjects.messengerbusinesstemplate import MessengerBusinessTemplate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMessengerBusinessTemplate"
instructions = """
MessengerBusinessTemplate MCP Server for Facebook Business API.

Provides typed access to all MessengerBusinessTemplate operations.
"""

messengerbusinesstemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@messengerbusinesstemplate_server.tool
@wrapped_fn_tool
def get_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
) -> str:
    obj = MessengerBusinessTemplate(messengerbusinesstemplate_id)
    return obj.api_get(fields=fields)


@messengerbusinesstemplate_server.tool
@wrapped_fn_tool
def update_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return MessengerBusinessTemplate(messengerbusinesstemplate_id).api_update(
        fields=fields, params=params
    )
