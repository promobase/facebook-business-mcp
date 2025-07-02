"""
Auto-generated MCP server for Facebook MailingAddress.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mailingaddress import MailingAddress
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mailingaddress")


# CRUD Operations


@mcp.tool()
async def api_create_mailingaddress(
    mailingaddress_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MailingAddress(fbid=mailingaddress_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_mailingaddress(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MailingAddress(fbid=mailingaddress_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_mailingaddress(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MailingAddress(fbid=mailingaddress_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_mailingaddress(
    mailingaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MailingAddress(fbid=mailingaddress_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mailingaddress_server = mcp
