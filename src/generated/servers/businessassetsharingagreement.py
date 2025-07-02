"""
Auto-generated MCP server for Facebook BusinessAssetSharingAgreement.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessassetsharingagreement")


# CRUD Operations


@mcp.tool()
async def get_businessassetsharingagreement(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessAssetSharingAgreement.

    Args:
        object_id: The ID of the BusinessAssetSharingAgreement
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessAssetSharingAgreement(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessassetsharingagreement(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a BusinessAssetSharingAgreement.

    Args:
        object_id: The ID of the BusinessAssetSharingAgreement
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = BusinessAssetSharingAgreement(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessassetsharingagreement_server = mcp
