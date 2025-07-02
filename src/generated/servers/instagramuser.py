"""
Auto-generated MCP server for Facebook InstagramUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramuser import InstagramUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramuser")


# CRUD Operations


@mcp.tool()
async def create_instagramuser(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_agencies_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ar_effects_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).get_ar_effects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_authorized_ad_accounts_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_upcoming_events_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramUser(fbid=object_id).get_upcoming_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramuser_server = mcp
