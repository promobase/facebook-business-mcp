"""
Auto-generated MCP server for Facebook PageDirectIntegrationCrmWithLeadsAccess.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagedirectintegrationcrmwithleadsaccess import (
    PageDirectIntegrationCrmWithLeadsAccess,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagedirectintegrationcrmwithleadsaccess")


# CRUD Operations


@mcp.tool()
async def create_pagedirectintegrationcrmwithleadsaccess(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_pagedirectintegrationcrmwithleadsaccess(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pagedirectintegrationcrmwithleadsaccess(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_pagedirectintegrationcrmwithleadsaccess(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagedirectintegrationcrmwithleadsaccess_server = mcp
