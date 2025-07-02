"""
Auto-generated MCP server for Facebook IGUserExportForCAM.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguserexportforcam import IGUserExportForCAM
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguserexportforcam")


# CRUD Operations


@mcp.tool()
async def get_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGUserExportForCAM.

    Args:
        object_id: The ID of the IGUserExportForCAM
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGUserExportForCAM(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_branded_content_media_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Branded Content Media for IGUserExportForCAM.

    Args:
        object_id: The ID of the IGUserExportForCAM
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_branded_content_media result
    """
    result = IGUserExportForCAM(fbid=object_id).get_branded_content_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for IGUserExportForCAM.

    Args:
        object_id: The ID of the IGUserExportForCAM
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = IGUserExportForCAM(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recent_media_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Recent Media for IGUserExportForCAM.

    Args:
        object_id: The ID of the IGUserExportForCAM
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_recent_media result
    """
    result = IGUserExportForCAM(fbid=object_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserexportforcam_server = mcp
