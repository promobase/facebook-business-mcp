"""WhatsAppBusinessProfile MCP Server."""

from typing import Any

from facebook_business.adobjects.whatsappbusinessprofile import WhatsAppBusinessProfile
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWhatsAppBusinessProfile"
instructions = """
WhatsAppBusinessProfile MCP Server for Facebook Business API.

Provides typed access to all WhatsAppBusinessProfile operations.
"""

whatsappbusinessprofile_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@whatsappbusinessprofile_server.tool
@wrapped_fn_tool
def get_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[str] = [],
) -> str:
    obj = WhatsAppBusinessProfile(whatsappbusinessprofile_id)
    return obj.api_get(fields=fields)


@whatsappbusinessprofile_server.tool
@wrapped_fn_tool
def update_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return WhatsAppBusinessProfile(whatsappbusinessprofile_id).api_update(
        fields=fields, params=params
    )
