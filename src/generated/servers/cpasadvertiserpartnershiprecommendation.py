"""
Auto-generated MCP server for Facebook CPASAdvertiserPartnershipRecommendation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasadvertiserpartnershiprecommendation import (
    CPASAdvertiserPartnershipRecommendation,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasadvertiserpartnershiprecommendation")


# CRUD Operations


@mcp.tool()
async def get_cpasadvertiserpartnershiprecommendation(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASAdvertiserPartnershipRecommendation.

    Args:
        object_id: The ID of the CPASAdvertiserPartnershipRecommendation
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASAdvertiserPartnershipRecommendation(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasadvertiserpartnershiprecommendation_server = mcp
