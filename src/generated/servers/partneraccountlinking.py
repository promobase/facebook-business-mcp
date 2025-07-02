"""
Auto-generated MCP server for Facebook PartnerAccountLinking.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partneraccountlinking import PartnerAccountLinking
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-partneraccountlinking")


# CRUD Operations


@mcp.tool()
async def create_partneraccountlinking(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerAccountLinking(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_partneraccountlinking(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerAccountLinking(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_partneraccountlinking(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerAccountLinking(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_partneraccountlinking(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerAccountLinking(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partneraccountlinking_server = mcp
