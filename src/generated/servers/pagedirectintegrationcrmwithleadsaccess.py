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
async def api_create_pagedirectintegrationcrmwithleadsaccess(
    pagedirectintegrationcrmwithleadsaccess_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(
        fbid=pagedirectintegrationcrmwithleadsaccess_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagedirectintegrationcrmwithleadsaccess(
    pagedirectintegrationcrmwithleadsaccess_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(
        fbid=pagedirectintegrationcrmwithleadsaccess_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagedirectintegrationcrmwithleadsaccess(
    pagedirectintegrationcrmwithleadsaccess_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(
        fbid=pagedirectintegrationcrmwithleadsaccess_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagedirectintegrationcrmwithleadsaccess(
    pagedirectintegrationcrmwithleadsaccess_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageDirectIntegrationCrmWithLeadsAccess(
        fbid=pagedirectintegrationcrmwithleadsaccess_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagedirectintegrationcrmwithleadsaccess_server = mcp
