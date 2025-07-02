"""
Auto-generated MCP server for Facebook CopyrightOwnershipTransfer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.copyrightownershiptransfer import CopyrightOwnershipTransfer
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-copyrightownershiptransfer")


# CRUD Operations


@mcp.tool()
async def get_copyrightownershiptransfer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CopyrightOwnershipTransfer.

    Args:
        object_id: The ID of the CopyrightOwnershipTransfer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CopyrightOwnershipTransfer(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
copyrightownershiptransfer_server = mcp
