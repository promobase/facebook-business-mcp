"""
Auto-generated MCP server for Facebook ProductFeedUploadError.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeeduploaderror import ProductFeedUploadError
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeeduploaderror")


# CRUD Operations


@mcp.tool()
async def get_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeedUploadError.

    Args:
        object_id: The ID of the ProductFeedUploadError
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeedUploadError(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_samples_for_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Samples for ProductFeedUploadError.

    Args:
        object_id: The ID of the ProductFeedUploadError
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_samples result
    """
    result = ProductFeedUploadError(fbid=object_id).get_samples(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_suggested_rules_for_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Suggested Rules for ProductFeedUploadError.

    Args:
        object_id: The ID of the ProductFeedUploadError
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_suggested_rules result
    """
    result = ProductFeedUploadError(fbid=object_id).get_suggested_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeeduploaderror_server = mcp
