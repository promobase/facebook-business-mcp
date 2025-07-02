"""
Auto-generated MCP server for Facebook ExtendedCreditApplication.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcreditapplication import ExtendedCreditApplication
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcreditapplication")


# CRUD Operations


@mcp.tool()
async def get_extendedcreditapplication(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ExtendedCreditApplication.

    Args:
        object_id: The ID of the ExtendedCreditApplication
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ExtendedCreditApplication(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcreditapplication_server = mcp
