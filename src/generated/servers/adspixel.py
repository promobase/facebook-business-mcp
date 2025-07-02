"""
Auto-generated MCP server for Facebook AdsPixel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adspixel")


# CRUD Operations


@mcp.tool()
async def create_adspixel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_agency_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ahp_config_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_ahp_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_event_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_event(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shadow_traffic_helper_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_shadow_traffic_helper(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shared_account_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_shared_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).delete_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_da_checks_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_da_checks(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offline_event_uploads_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_offline_event_uploads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_open_bridge_configurations_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_open_bridge_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_shared_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stats_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=object_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspixel_server = mcp
