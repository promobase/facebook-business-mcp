"""
Auto-generated MCP server for Facebook InstagramUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramuser import InstagramUser
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramuser")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    instagramuser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_agencies(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ar_effects(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).get_ar_effects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_authorized_ad_accounts(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_upcoming_events(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramUser(fbid=instagramuser_id).get_upcoming_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramuser_server = mcp
