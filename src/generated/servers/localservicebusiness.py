"""
Auto-generated MCP server for Facebook LocalServiceBusiness.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.localservicebusiness import LocalServiceBusiness
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-localservicebusiness")


# CRUD Operations


@mcp.tool()
async def api_create_localservicebusiness(
    localservicebusiness_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_localservicebusiness(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_localservicebusiness(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_localservicebusiness(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LocalServiceBusiness(fbid=localservicebusiness_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
localservicebusiness_server = mcp
