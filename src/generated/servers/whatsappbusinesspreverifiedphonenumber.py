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
async def create_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_request_code_for_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).create_request_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_verify_code_for_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).create_verify_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partners_for_whatsappbusinesspreverifiedphonenumber(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPreVerifiedPhoneNumber(fbid=object_id).get_partners(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinesspreverifiedphonenumber_server = mcp
