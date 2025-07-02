"""
Auto-generated MCP server for Facebook PageInsightsAsyncExportRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageinsightsasyncexportrun import PageInsightsAsyncExportRun
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageinsightsasyncexportrun")


# CRUD Operations


@mcp.tool()
async def get_pageinsightsasyncexportrun(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PageInsightsAsyncExportRun.

    Args:
        object_id: The ID of the PageInsightsAsyncExportRun
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PageInsightsAsyncExportRun(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageinsightsasyncexportrun_server = mcp
