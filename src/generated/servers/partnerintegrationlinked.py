"""
Auto-generated MCP server for Facebook PartnerIntegrationLinked.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-partnerintegrationlinked")


# CRUD Operations


@mcp.tool()
async def api_create_partnerintegrationlinked(
    partnerintegrationlinked_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerIntegrationLinked(fbid=partnerintegrationlinked_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_partnerintegrationlinked(
    partnerintegrationlinked_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerIntegrationLinked(fbid=partnerintegrationlinked_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_partnerintegrationlinked(
    partnerintegrationlinked_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerIntegrationLinked(fbid=partnerintegrationlinked_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_partnerintegrationlinked(
    partnerintegrationlinked_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerIntegrationLinked(fbid=partnerintegrationlinked_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partnerintegrationlinked_server = mcp
