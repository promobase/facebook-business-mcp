"""
Auto-generated MCP server for Facebook WhatsAppBusinessProfile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinessprofile import WhatsAppBusinessProfile
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinessprofile")


# CRUD Operations


@mcp.tool()
async def api_create_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessProfile(fbid=whatsappbusinessprofile_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessProfile(fbid=whatsappbusinessprofile_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessProfile(fbid=whatsappbusinessprofile_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_whatsappbusinessprofile(
    whatsappbusinessprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessProfile(fbid=whatsappbusinessprofile_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinessprofile_server = mcp
