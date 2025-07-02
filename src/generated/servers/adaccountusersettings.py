"""
Auto-generated MCP server for Facebook AdAccountUserSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountusersettings import AdAccountUserSettings
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountusersettings")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountusersettings(
    adaccountusersettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUserSettings(fbid=adaccountusersettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountusersettings(
    adaccountusersettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUserSettings(fbid=adaccountusersettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountusersettings(
    adaccountusersettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUserSettings(fbid=adaccountusersettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountusersettings(
    adaccountusersettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUserSettings(fbid=adaccountusersettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountusersettings_server = mcp
