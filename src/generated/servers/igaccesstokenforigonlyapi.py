"""
Auto-generated MCP server for Facebook IGAccessTokenForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igaccesstokenforigonlyapi import IGAccessTokenForIGOnlyAPI
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igaccesstokenforigonlyapi")


# CRUD Operations


@mcp.tool()
async def get_igaccesstokenforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGAccessTokenForIGOnlyAPI.

    Args:
        object_id: The ID of the IGAccessTokenForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGAccessTokenForIGOnlyAPI(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igaccesstokenforigonlyapi_server = mcp
