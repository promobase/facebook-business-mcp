"""WhatsAppBusinessPreVerifiedPhoneNumber MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.whatsappbusinesspreverifiedphonenumber import (
    WhatsAppBusinessPreVerifiedPhoneNumber,
)
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.whatsappbusinesspreverifiedphonenumber import (
    WhatsAppBusinessPreVerifiedPhoneNumberCreateRequestCodeParams,
    WhatsAppBusinessPreVerifiedPhoneNumberCreateVerifyCodeParams,
    WhatsAppBusinessPreVerifiedPhoneNumberField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWhatsAppBusinessPreVerifiedPhoneNumber"
instructions = """
WhatsAppBusinessPreVerifiedPhoneNumber MCP Server for Facebook Business API.

Provides typed access to all WhatsAppBusinessPreVerifiedPhoneNumber operations.
"""

whatsappbusinesspreverifiedphonenumber_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def get_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[WhatsAppBusinessPreVerifiedPhoneNumberField] = [],
) -> str:
    """Get a WhatsAppBusinessPreVerifiedPhoneNumber object by ID.

    Args:
        whatsappbusinesspreverifiedphonenumber_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber.
        fields: Fields to retrieve. Available fields: See WhatsAppBusinessPreVerifiedPhoneNumberField type.
    """
    obj = WhatsAppBusinessPreVerifiedPhoneNumber(whatsappbusinesspreverifiedphonenumber_id)
    return obj.api_get(fields=fields)


@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def delete_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
) -> str:
    """Delete a WhatsAppBusinessPreVerifiedPhoneNumber object.

    Args:
        whatsappbusinesspreverifiedphonenumber_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber.
    """
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).api_delete()


# ---- Edge Methods (2) ----
@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def create_request_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessPreVerifiedPhoneNumberCreateRequestCodeParams | dict = {},
):
    """Create Request Code for this WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whatsappbusinesspreverifiedphonenumber_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessPreVerifiedPhoneNumberCreateRequestCodeParams type.
    """
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).create_request_code(fields=fields, params=params)


@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def create_verify_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: WhatsAppBusinessPreVerifiedPhoneNumberCreateVerifyCodeParams | dict = {},
):
    """Create Verify Code for this WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whatsappbusinesspreverifiedphonenumber_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See WhatsAppBusinessPreVerifiedPhoneNumberCreateVerifyCodeParams type.
    """
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).create_verify_code(fields=fields, params=params)
