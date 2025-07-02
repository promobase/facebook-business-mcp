"""
Auto-generated MCP server for Facebook PartnerAccountLinking.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partneraccountlinking import PartnerAccountLinking
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-partneraccountlinking")


# CRUD Operations


@mcp.tool()
async def get_partneraccountlinking(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PartnerAccountLinking.

    Args:
        object_id: The ID of the PartnerAccountLinking
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PartnerAccountLinking(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partneraccountlinking_server = mcp
