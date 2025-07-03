"""
Auto-generated MCP server for Facebook UserPageOneTimeOptInTokenSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettings,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-userpageonetimeoptintokensettings")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    userpageonetimeoptintokensettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserPageOneTimeOptInTokenSettings(fbid=userpageonetimeoptintokensettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    userpageonetimeoptintokensettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserPageOneTimeOptInTokenSettings(
        fbid=userpageonetimeoptintokensettings_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
userpageonetimeoptintokensettings_server = mcp
