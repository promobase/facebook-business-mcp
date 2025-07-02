"""
Auto-generated MCP server for Facebook UserPageOneTimeOptInTokenSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettings,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-userpageonetimeoptintokensettings")


# CRUD Operations


@mcp.tool()
async def api_create_userpageonetimeoptintokensettings(
    userpageonetimeoptintokensettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_userpageonetimeoptintokensettings(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_userpageonetimeoptintokensettings(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserPageOneTimeOptInTokenSettings(fbid=userpageonetimeoptintokensettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_userpageonetimeoptintokensettings(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
userpageonetimeoptintokensettings_server = mcp
