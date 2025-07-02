"""
Auto-generated MCP server for Facebook WhatsAppBusinessPreVerifiedPhoneNumber.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinesspreverifiedphonenumber import (
    WhatsAppBusinessPreVerifiedPhoneNumber,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinesspreverifiedphonenumber")


# CRUD Operations


@mcp.tool()
async def api_create_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_whatsappbusinesspreverifiedphonenumber(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_request_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).create_request_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_verify_code(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).create_verify_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partners(
    whatsappbusinesspreverifiedphonenumber_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(
        fbid=whatsappbusinesspreverifiedphonenumber_id
    ).get_partners(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinesspreverifiedphonenumber_server = mcp
