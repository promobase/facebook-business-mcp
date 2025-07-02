"""
Auto-generated MCP server for Facebook ProductFeedUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedupload import ProductFeedUpload
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedupload")


# CRUD Operations


@mcp.tool()
async def get_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeedUpload.

    Args:
        object_id: The ID of the ProductFeedUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeedUpload(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_error_report_for_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Error Report for ProductFeedUpload.

    Args:
        object_id: The ID of the ProductFeedUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_error_report result
    """
    result = ProductFeedUpload(fbid=object_id).create_error_report(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_errors_for_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Errors for ProductFeedUpload.

    Args:
        object_id: The ID of the ProductFeedUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_errors result
    """
    result = ProductFeedUpload(fbid=object_id).get_errors(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedupload_server = mcp
