"""
Auto-generated MCP server for Facebook AdReportRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adreportrun import AdReportRun
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adreportrun")


# CRUD Operations


@mcp.tool()
async def create_adreportrun(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdReportRun.

    Args:
        object_id: The ID of the AdReportRun
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdReportRun(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adreportrun(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdReportRun.

    Args:
        object_id: The ID of the AdReportRun
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdReportRun(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_insights_for_adreportrun(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for AdReportRun.

    Args:
        object_id: The ID of the AdReportRun
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = AdReportRun(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adreportrun_server = mcp
