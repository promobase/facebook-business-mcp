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
async def api_create_adspixel(
    adspixel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_agency(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ahp_config(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_ahp_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_event(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_event(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shadow_traffic_helper(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_shadow_traffic_helper(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shared_account(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_shared_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).delete_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_da_checks(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_da_checks(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offline_event_uploads(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_offline_event_uploads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_open_bridge_configurations(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_open_bridge_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_agencies(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_shared_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stats(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPixel(fbid=adspixel_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspixel_server = mcp
