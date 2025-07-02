"""
Auto-generated MCP server for Facebook ProductFeedUploadErrorSample.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeeduploaderrorsample import ProductFeedUploadErrorSample
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeeduploaderrorsample")


# CRUD Operations


@mcp.tool()
async def get_productfeeduploaderrorsample(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeedUploadErrorSample.

    Args:
        object_id: The ID of the ProductFeedUploadErrorSample
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeedUploadErrorSample(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeeduploaderrorsample_server = mcp
