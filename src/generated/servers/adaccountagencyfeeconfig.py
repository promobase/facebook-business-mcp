"""
Auto-generated MCP server for Facebook AdAccountAgencyFeeConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountagencyfeeconfig import AdAccountAgencyFeeConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountagencyfeeconfig")


# CRUD Operations


@mcp.tool()
async def get_adaccountagencyfeeconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdAccountAgencyFeeConfig.

    Args:
        object_id: The ID of the AdAccountAgencyFeeConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdAccountAgencyFeeConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountagencyfeeconfig_server = mcp
