"""
Auto-generated MCP server for Facebook WhatsAppBusinessProfile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whatsappbusinessprofile import WhatsAppBusinessProfile
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whatsappbusinessprofile")


# CRUD Operations


@mcp.tool()
async def get_whatsappbusinessprofile(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WhatsAppBusinessProfile.

    Args:
        object_id: The ID of the WhatsAppBusinessProfile
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WhatsAppBusinessProfile(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_whatsappbusinessprofile(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a WhatsAppBusinessProfile.

    Args:
        object_id: The ID of the WhatsAppBusinessProfile
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = WhatsAppBusinessProfile(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whatsappbusinessprofile_server = mcp
