"""
Auto-generated MCP server for Facebook AdMonetizationProperty.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-admonetizationproperty")


# CRUD Operations


@mcp.tool()
async def get_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdMonetizationProperty.

    Args:
        object_id: The ID of the AdMonetizationProperty
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdMonetizationProperty(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_network_analytic_for_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Network Analytic for AdMonetizationProperty.

    Args:
        object_id: The ID of the AdMonetizationProperty
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_network_analytic result
    """
    result = AdMonetizationProperty(fbid=object_id).create_ad_network_analytic(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_for_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Network Analytics for AdMonetizationProperty.

    Args:
        object_id: The ID of the AdMonetizationProperty
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics result
    """
    result = AdMonetizationProperty(fbid=object_id).get_ad_network_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_results_for_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Network Analytics Results for AdMonetizationProperty.

    Args:
        object_id: The ID of the AdMonetizationProperty
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_network_analytics_results result
    """
    result = AdMonetizationProperty(fbid=object_id).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


# Export the server
admonetizationproperty_server = mcp
