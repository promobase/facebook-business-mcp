"""
Auto-generated MCP server for Facebook LeadGenDirectCRMIntegrationConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgendirectcrmintegrationconfig import (
    LeadGenDirectCRMIntegrationConfig,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgendirectcrmintegrationconfig")


# CRUD Operations


@mcp.tool()
async def get_leadgendirectcrmintegrationconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LeadGenDirectCRMIntegrationConfig.

    Args:
        object_id: The ID of the LeadGenDirectCRMIntegrationConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LeadGenDirectCRMIntegrationConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgendirectcrmintegrationconfig_server = mcp
