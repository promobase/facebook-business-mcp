"""
Auto-generated MCP server for Facebook AdsStartYourDayWidget.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsstartyourdaywidget import AdsStartYourDayWidget
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsstartyourdaywidget")


# CRUD Operations


@mcp.tool()
async def get_adsstartyourdaywidget(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsStartYourDayWidget.

    Args:
        object_id: The ID of the AdsStartYourDayWidget
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsStartYourDayWidget(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsstartyourdaywidget_server = mcp
