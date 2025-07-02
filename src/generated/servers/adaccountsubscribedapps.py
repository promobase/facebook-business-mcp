"""
Auto-generated MCP server for Facebook AdAccountSubscribedApps.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountsubscribedapps import AdAccountSubscribedApps
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountsubscribedapps")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountsubscribedapps(
    adaccountsubscribedapps_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountSubscribedApps(fbid=adaccountsubscribedapps_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountsubscribedapps(
    adaccountsubscribedapps_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountSubscribedApps(fbid=adaccountsubscribedapps_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountsubscribedapps(
    adaccountsubscribedapps_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountSubscribedApps(fbid=adaccountsubscribedapps_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountsubscribedapps(
    adaccountsubscribedapps_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountSubscribedApps(fbid=adaccountsubscribedapps_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountsubscribedapps_server = mcp
