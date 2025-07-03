"""
Auto-generated MCP server for Facebook OfflineConversionDataSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondataset")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    offlineconversiondataset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_agencies(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_audiences(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_audiences(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_custom_conversions(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_server_events_permitted_business(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(
        fbid=offlineconversiondataset_id
    ).get_server_events_permitted_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_accounts(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_agencies(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_shared_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_stats(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_uploads(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSet(fbid=offlineconversiondataset_id).get_uploads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondataset_server = mcp
