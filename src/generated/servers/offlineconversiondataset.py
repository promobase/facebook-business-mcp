"""
Auto-generated MCP server for Facebook OfflineConversionDataSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondataset")


# CRUD Operations


@mcp.tool()
async def get_offlineconversiondataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OfflineConversionDataSet(fbid=object_id).api_get(
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
    """
    Get Ad Accounts for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
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
    """
    Get Agencies for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
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
    """
    Get Audiences for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_audiences result
    """
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
    """
    Get Custom Conversions for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_conversions result
    """
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
    """
    Get Server Events Permitted Business for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_server_events_permitted_business result
    """
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
    """
    Get Shared Accounts for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_accounts result
    """
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
    """
    Get Shared Agencies for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_agencies result
    """
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
    """
    Get Stats for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stats result
    """
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
    """
    Get Uploads for OfflineConversionDataSet.

    Args:
        object_id: The ID of the OfflineConversionDataSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_uploads result
    """
    result = OfflineConversionDataSet(fbid=object_id).get_uploads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondataset_server = mcp
