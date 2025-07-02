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
async def create_crmaddress(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_crmaddress(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crmaddress(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_crmaddress(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CRMAddress(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
crmaddress_server = mcp
