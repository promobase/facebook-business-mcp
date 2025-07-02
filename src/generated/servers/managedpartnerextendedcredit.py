"""
Auto-generated MCP server for Facebook ManagedPartnerExtendedCredit.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managedpartnerextendedcredit import ManagedPartnerExtendedCredit
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-managedpartnerextendedcredit")


# CRUD Operations


@mcp.tool()
async def api_create_managedpartnerextendedcredit(
    managedpartnerextendedcredit_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerExtendedCredit(fbid=managedpartnerextendedcredit_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_managedpartnerextendedcredit(
    managedpartnerextendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerExtendedCredit(fbid=managedpartnerextendedcredit_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_managedpartnerextendedcredit(
    managedpartnerextendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerExtendedCredit(fbid=managedpartnerextendedcredit_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_managedpartnerextendedcredit(
    managedpartnerextendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerExtendedCredit(fbid=managedpartnerextendedcredit_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managedpartnerextendedcredit_server = mcp
