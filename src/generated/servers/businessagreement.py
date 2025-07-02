"""
Auto-generated MCP server for Facebook BusinessAgreement.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessagreement import BusinessAgreement
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessagreement")


# CRUD Operations


@mcp.tool()
async def get_businessagreement(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessAgreement.

    Args:
        object_id: The ID of the BusinessAgreement
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessAgreement(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessagreement(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a BusinessAgreement.

    Args:
        object_id: The ID of the BusinessAgreement
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = BusinessAgreement(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessagreement_server = mcp
