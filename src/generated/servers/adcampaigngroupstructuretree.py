"""
Auto-generated MCP server for Facebook AdCampaignGroupStructureTree.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcampaigngroupstructuretree import AdCampaignGroupStructureTree
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcampaigngroupstructuretree")


# CRUD Operations


@mcp.tool()
async def api_create_adcampaigngroupstructuretree(
    adcampaigngroupstructuretree_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCampaignGroupStructureTree(fbid=adcampaigngroupstructuretree_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcampaigngroupstructuretree(
    adcampaigngroupstructuretree_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCampaignGroupStructureTree(fbid=adcampaigngroupstructuretree_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcampaigngroupstructuretree(
    adcampaigngroupstructuretree_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCampaignGroupStructureTree(fbid=adcampaigngroupstructuretree_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcampaigngroupstructuretree(
    adcampaigngroupstructuretree_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCampaignGroupStructureTree(fbid=adcampaigngroupstructuretree_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcampaigngroupstructuretree_server = mcp
