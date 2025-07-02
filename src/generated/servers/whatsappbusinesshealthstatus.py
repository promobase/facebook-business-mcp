"""
Auto-generated MCP server for Facebook WhatsAppBusinessHealthStatus.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinesshealthstatus import WhatsAppBusinessHealthStatus
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinesshealthstatus")


# CRUD Operations


@mcp.tool()
async def api_create_whatsappbusinesshealthstatus(
    whatsappbusinesshealthstatus_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessHealthStatus(fbid=whatsappbusinesshealthstatus_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_whatsappbusinesshealthstatus(
    whatsappbusinesshealthstatus_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessHealthStatus(fbid=whatsappbusinesshealthstatus_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_whatsappbusinesshealthstatus(
    whatsappbusinesshealthstatus_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessHealthStatus(fbid=whatsappbusinesshealthstatus_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_whatsappbusinesshealthstatus(
    whatsappbusinesshealthstatus_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WhatsAppBusinessHealthStatus(fbid=whatsappbusinesshealthstatus_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinesshealthstatus_server = mcp
