"""
Auto-generated MCP server for Facebook WhatsAppBusinessPartnerClientVerificationSubmission.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinesspartnerclientverificationsubmission import (
    WhatsAppBusinessPartnerClientVerificationSubmission,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinesspartnerclientverificationsubmission")


# CRUD Operations


@mcp.tool()
async def api_create_whatsappbusinesspartnerclientverificationsubmission(
    whatsappbusinesspartnerclientverificationsubmission_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPartnerClientVerificationSubmission(
        fbid=whatsappbusinesspartnerclientverificationsubmission_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_whatsappbusinesspartnerclientverificationsubmission(
    whatsappbusinesspartnerclientverificationsubmission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPartnerClientVerificationSubmission(
        fbid=whatsappbusinesspartnerclientverificationsubmission_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_whatsappbusinesspartnerclientverificationsubmission(
    whatsappbusinesspartnerclientverificationsubmission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPartnerClientVerificationSubmission(
        fbid=whatsappbusinesspartnerclientverificationsubmission_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_whatsappbusinesspartnerclientverificationsubmission(
    whatsappbusinesspartnerclientverificationsubmission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessPartnerClientVerificationSubmission(
        fbid=whatsappbusinesspartnerclientverificationsubmission_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinesspartnerclientverificationsubmission_server = mcp
