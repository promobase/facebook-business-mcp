"""MessengerBusinessTemplate MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.messengerbusinesstemplate import MessengerBusinessTemplate
from fastmcp import FastMCP

from src.generated.models.messengerbusinesstemplate import (
    MessengerBusinessTemplateField,
    MessengerBusinessTemplateUpdateParams,
)
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
    fields: list[MessengerBusinessTemplateField] = [],
) -> str:
    """Get a MessengerBusinessTemplate object by ID.

    Args:
        messengerbusinesstemplate_id: The ID of the MessengerBusinessTemplate.
        fields: Fields to retrieve. Available fields: See MessengerBusinessTemplateField type.
    """
    obj = MessengerBusinessTemplate(messengerbusinesstemplate_id)
    return obj.api_get(fields=fields)


@messengerbusinesstemplate_server.tool
@wrapped_fn_tool
def update_messengerbusinesstemplate(
    messengerbusinesstemplate_id: str,
    fields: list[MessengerBusinessTemplateField] = [],
    params: MessengerBusinessTemplateUpdateParams | dict = {},
) -> str:
    """Update a MessengerBusinessTemplate object.

    Args:
        messengerbusinesstemplate_id: The ID of the MessengerBusinessTemplate.
        fields: Fields to return after update. Available fields: See MessengerBusinessTemplateField type.
        params: Parameters to update. Available params: See MessengerBusinessTemplateUpdateParams type.
    """
    return MessengerBusinessTemplate(messengerbusinesstemplate_id).api_update(
        fields=fields, params=params
    )
