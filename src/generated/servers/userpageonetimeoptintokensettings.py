"""
Auto-generated MCP server for Facebook UserPageOneTimeOptInTokenSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.userpageonetimeoptintokensettings import (
    UserPageOneTimeOptInTokenSettings,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-userpageonetimeoptintokensettings")


# CRUD Operations


@mcp.tool()
async def get_userpageonetimeoptintokensettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a UserPageOneTimeOptInTokenSettings.

    Args:
        object_id: The ID of the UserPageOneTimeOptInTokenSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = UserPageOneTimeOptInTokenSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
userpageonetimeoptintokensettings_server = mcp
