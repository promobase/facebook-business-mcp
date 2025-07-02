"""
Auto-generated MCP server for Facebook CPASMerchantConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasmerchantconfig import CPASMerchantConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasmerchantconfig")


# CRUD Operations


@mcp.tool()
async def get_cpasmerchantconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASMerchantConfig.

    Args:
        object_id: The ID of the CPASMerchantConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASMerchantConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasmerchantconfig_server = mcp
