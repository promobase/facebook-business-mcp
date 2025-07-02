"""
Auto-generated MCP server for Facebook BusinessObjectTransferOwnershipAgreement.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessobjecttransferownershipagreement import (
    BusinessObjectTransferOwnershipAgreement,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessobjecttransferownershipagreement")


# CRUD Operations


@mcp.tool()
async def get_businessobjecttransferownershipagreement(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessObjectTransferOwnershipAgreement.

    Args:
        object_id: The ID of the BusinessObjectTransferOwnershipAgreement
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessObjectTransferOwnershipAgreement(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessobjecttransferownershipagreement_server = mcp
