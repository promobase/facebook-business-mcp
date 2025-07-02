"""
Auto-generated MCP server for Facebook AdsConversionGoal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsconversiongoal import AdsConversionGoal
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsconversiongoal")


# CRUD Operations


@mcp.tool()
async def get_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsConversionGoal.

    Args:
        object_id: The ID of the AdsConversionGoal
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsConversionGoal(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_conversion_events_for_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Conversion Events for AdsConversionGoal.

    Args:
        object_id: The ID of the AdsConversionGoal
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversion_events result
    """
    result = AdsConversionGoal(fbid=object_id).get_conversion_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsconversiongoal_server = mcp
