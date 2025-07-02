"""WhatsAppBusinessPreVerifiedPhoneNumber MCP Server."""

from typing import Any

from facebook_business.adobjects.whatsappbusinesspreverifiedphonenumber import (
    WhatsAppBusinessPreVerifiedPhoneNumber,
)
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = WhatsAppBusinessPreVerifiedPhoneNumber(whatsappbusinesspreverifiedphonenumber_id)
    return obj.api_get(fields=fields)


@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def delete_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
) -> str:
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).api_delete()


# ---- Edge Methods (3) ----
@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def get_partners(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).get_partners(fields=fields, params=params)


@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def create_request_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).create_request_code(fields=fields, params=params)


@whatsappbusinesspreverifiedphonenumber_server.tool
@wrapped_fn_tool
def create_verify_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return WhatsAppBusinessPreVerifiedPhoneNumber(
        whatsappbusinesspreverifiedphonenumber_id
    ).create_verify_code(fields=fields, params=params)
