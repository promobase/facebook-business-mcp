"""
Auto-generated MCP server for Facebook ManagedPartnerBusiness.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managedpartnerbusiness import ManagedPartnerBusiness
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-managedpartnerbusiness")


# CRUD Operations


@mcp.tool()
async def api_create_managedpartnerbusiness(
    managedpartnerbusiness_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_managedpartnerbusiness(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_managedpartnerbusiness(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_managedpartnerbusiness(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managedpartnerbusiness_server = mcp
