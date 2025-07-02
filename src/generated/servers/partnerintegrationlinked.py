"""
Auto-generated MCP server for Facebook PartnerIntegrationLinked.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-partnerintegrationlinked")


# CRUD Operations


@mcp.tool()
async def get_partnerintegrationlinked(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PartnerIntegrationLinked.

    Args:
        object_id: The ID of the PartnerIntegrationLinked
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PartnerIntegrationLinked(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partnerintegrationlinked_server = mcp
