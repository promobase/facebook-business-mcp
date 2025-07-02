"""
Auto-generated MCP server for Facebook BCPCampaign.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bcpcampaign import BCPCampaign
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bcpcampaign")


# CRUD Operations


@mcp.tool()
async def api_create_bcpcampaign(
    bcpcampaign_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BCPCampaign(fbid=bcpcampaign_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_bcpcampaign(
    bcpcampaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BCPCampaign(fbid=bcpcampaign_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_bcpcampaign(
    bcpcampaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BCPCampaign(fbid=bcpcampaign_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_bcpcampaign(
    bcpcampaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BCPCampaign(fbid=bcpcampaign_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bcpcampaign_server = mcp
