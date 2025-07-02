"""
Auto-generated MCP server for Facebook OfflineConversionDataSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondataset")


# CRUD Operations


@mcp.tool()
async def create_offlineconversiondataset(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_audiences_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_audiences(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_conversions_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_server_events_permitted_business_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_server_events_permitted_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_agencies_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_shared_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stats_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_uploads_for_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSet(fbid=object_id).get_uploads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondataset_server = mcp
