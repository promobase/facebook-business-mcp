"""
Auto-generated MCP server for Facebook MediaCopyrightUpdateRecord.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediacopyrightupdaterecord import MediaCopyrightUpdateRecord
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mediacopyrightupdaterecord")


# CRUD Operations


@mcp.tool()
async def get_mediacopyrightupdaterecord(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MediaCopyrightUpdateRecord.

    Args:
        object_id: The ID of the MediaCopyrightUpdateRecord
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MediaCopyrightUpdateRecord(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediacopyrightupdaterecord_server = mcp
