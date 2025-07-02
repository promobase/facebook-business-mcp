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
async def api_create_admonetizationproperty(
    admonetizationproperty_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_admonetizationproperty(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_admonetizationproperty(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_admonetizationproperty(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_network_analytic(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).create_ad_network_analytic(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(fbid=admonetizationproperty_id).get_ad_network_analytics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_network_analytics_results(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdMonetizationProperty(
        fbid=admonetizationproperty_id
    ).get_ad_network_analytics_results(
        fields=fields,
        params=params,
    )

    return result


# Export the server
admonetizationproperty_server = mcp
