"""
Auto-generated MCP server for Facebook WhitehatFBDLRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whitehatfbdlrun import WhitehatFBDLRun
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-whitehatfbdlrun")


# CRUD Operations


@mcp.tool()
async def get_whitehatfbdlrun(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WhitehatFBDLRun.

    Args:
        object_id: The ID of the WhitehatFBDLRun
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WhitehatFBDLRun(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whitehatfbdlrun_server = mcp
