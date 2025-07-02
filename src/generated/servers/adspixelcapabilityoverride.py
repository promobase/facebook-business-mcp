"""
Auto-generated MCP server for Facebook AdsPixelCapabilityOverride.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adspixelcapabilityoverride import AdsPixelCapabilityOverride
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adspixelcapabilityoverride")


# CRUD Operations


@mcp.tool()
async def api_create_adspixelcapabilityoverride(
    adspixelcapabilityoverride_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixelCapabilityOverride(fbid=adspixelcapabilityoverride_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adspixelcapabilityoverride(
    adspixelcapabilityoverride_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixelCapabilityOverride(fbid=adspixelcapabilityoverride_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adspixelcapabilityoverride(
    adspixelcapabilityoverride_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixelCapabilityOverride(fbid=adspixelcapabilityoverride_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adspixelcapabilityoverride(
    adspixelcapabilityoverride_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixelCapabilityOverride(fbid=adspixelcapabilityoverride_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspixelcapabilityoverride_server = mcp
