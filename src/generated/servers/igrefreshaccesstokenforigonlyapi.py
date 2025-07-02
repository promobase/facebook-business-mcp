"""
Auto-generated MCP server for Facebook IGRefreshAccessTokenForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igrefreshaccesstokenforigonlyapi import (
    IGRefreshAccessTokenForIGOnlyAPI,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igrefreshaccesstokenforigonlyapi")


# CRUD Operations


@mcp.tool()
async def get_igrefreshaccesstokenforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGRefreshAccessTokenForIGOnlyAPI.

    Args:
        object_id: The ID of the IGRefreshAccessTokenForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGRefreshAccessTokenForIGOnlyAPI(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igrefreshaccesstokenforigonlyapi_server = mcp
