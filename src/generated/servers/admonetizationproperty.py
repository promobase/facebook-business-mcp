"""
Auto-generated MCP server for Facebook AdMonetizationProperty.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-admonetizationproperty")


# CRUD Operations


@mcp.tool()
async def create_admonetizationproperty(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_admonetizationproperty(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=object_id).api_update(
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
    result = AdMonetizationProperty(fbid=object_id).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


# Export the server
admonetizationproperty_server = mcp
