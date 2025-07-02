"""
Auto-generated MCP server for Facebook AdLightCampaignGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adlightcampaigngroup import AdLightCampaignGroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adlightcampaigngroup")


# CRUD Operations


@mcp.tool()
async def api_create_adlightcampaigngroup(
    adlightcampaigngroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightCampaignGroup(fbid=adlightcampaigngroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adlightcampaigngroup(
    adlightcampaigngroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightCampaignGroup(fbid=adlightcampaigngroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adlightcampaigngroup(
    adlightcampaigngroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightCampaignGroup(fbid=adlightcampaigngroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adlightcampaigngroup(
    adlightcampaigngroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightCampaignGroup(fbid=adlightcampaigngroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adlightcampaigngroup_server = mcp
