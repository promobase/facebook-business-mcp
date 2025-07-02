"""
Auto-generated MCP server for Facebook RightsManagerDataExport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rightsmanagerdataexport import RightsManagerDataExport
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-rightsmanagerdataexport")


# CRUD Operations


@mcp.tool()
async def get_rightsmanagerdataexport(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a RightsManagerDataExport.

    Args:
        object_id: The ID of the RightsManagerDataExport
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = RightsManagerDataExport(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rightsmanagerdataexport_server = mcp
