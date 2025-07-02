"""
Auto-generated MCP server for Facebook MailingAddress.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mailingaddress import MailingAddress
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mailingaddress")


# CRUD Operations


@mcp.tool()
async def get_mailingaddress(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MailingAddress.

    Args:
        object_id: The ID of the MailingAddress
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MailingAddress(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mailingaddress_server = mcp
