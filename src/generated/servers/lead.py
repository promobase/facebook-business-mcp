"""
Auto-generated MCP server for Facebook Lead.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.lead import Lead
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-lead")


# CRUD Operations


@mcp.tool()
async def delete_lead(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Lead.

    Args:
        object_id: The ID of the Lead
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Lead(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_lead(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Lead.

    Args:
        object_id: The ID of the Lead
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Lead(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
lead_server = mcp
