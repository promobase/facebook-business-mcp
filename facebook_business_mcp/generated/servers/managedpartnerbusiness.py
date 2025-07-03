"""
Auto-generated MCP server for Facebook ManagedPartnerBusiness.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managedpartnerbusiness import ManagedPartnerBusiness
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-managedpartnerbusiness")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    managedpartnerbusiness_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagedPartnerBusiness(fbid=managedpartnerbusiness_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managedpartnerbusiness_server = mcp
