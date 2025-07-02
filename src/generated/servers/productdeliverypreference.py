"""
Auto-generated MCP server for Facebook ProductDeliveryPreference.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productdeliverypreference import ProductDeliveryPreference
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productdeliverypreference")


# CRUD Operations


@mcp.tool()
async def get_productdeliverypreference(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductDeliveryPreference.

    Args:
        object_id: The ID of the ProductDeliveryPreference
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductDeliveryPreference(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productdeliverypreference_server = mcp
