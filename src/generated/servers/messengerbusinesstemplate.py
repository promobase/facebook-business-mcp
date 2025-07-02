"""
Auto-generated MCP server for Facebook MessengerBusinessTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengerbusinesstemplate import MessengerBusinessTemplate
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-messengerbusinesstemplate")


# CRUD Operations


@mcp.tool()
async def get_messengerbusinesstemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MessengerBusinessTemplate.

    Args:
        object_id: The ID of the MessengerBusinessTemplate
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MessengerBusinessTemplate(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_messengerbusinesstemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a MessengerBusinessTemplate.

    Args:
        object_id: The ID of the MessengerBusinessTemplate
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = MessengerBusinessTemplate(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengerbusinesstemplate_server = mcp
