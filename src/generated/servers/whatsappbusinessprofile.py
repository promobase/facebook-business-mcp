"""WhatsAppBusinessProfile MCP Server with typed wrappers."""

from facebook_business.adobjects.whatsappbusinessprofile import WhatsAppBusinessProfile
from fastmcp import FastMCP

from src.generated.models.whatsappbusinessprofile import WhatsAppBusinessProfileField
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
    fields: list[WhatsAppBusinessProfileField] = [],
) -> str:
    """Get a WhatsAppBusinessProfile object by ID.

    Args:
        whatsappbusinessprofile_id: The ID of the WhatsAppBusinessProfile.
        fields: Fields to retrieve. Available fields: See WhatsAppBusinessProfileField type.
    """
    obj = WhatsAppBusinessProfile(whatsappbusinessprofile_id)
    return obj.api_get(fields=fields)


@whatsappbusinessprofile_server.tool
@wrapped_fn_tool
def update_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[WhatsAppBusinessProfileField] = [],
    params: dict = {},
) -> str:
    """Update a WhatsAppBusinessProfile object.

    Args:
        whatsappbusinessprofile_id: The ID of the WhatsAppBusinessProfile.
        fields: Fields to return after update. Available fields: See WhatsAppBusinessProfileField type.
        params: Parameters to update.
    """
    return WhatsAppBusinessProfile(whatsappbusinessprofile_id).api_update(
        fields=fields, params=params
    )
