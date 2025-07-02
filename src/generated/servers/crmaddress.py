"""
Auto-generated MCP server for Facebook CRMAddress.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.crmaddress import CRMAddress
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-crmaddress")


# CRUD Operations


@mcp.tool()
async def api_create_crmaddress(
    crmaddress_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=crmaddress_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_crmaddress(
    crmaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=crmaddress_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_crmaddress(
    crmaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=crmaddress_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_crmaddress(
    crmaddress_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=crmaddress_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
crmaddress_server = mcp
