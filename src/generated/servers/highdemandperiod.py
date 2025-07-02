"""
Auto-generated MCP server for Facebook HighDemandPeriod.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.highdemandperiod import HighDemandPeriod
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-highdemandperiod")


# CRUD Operations


@mcp.tool()
async def delete_highdemandperiod(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a HighDemandPeriod.

    Args:
        object_id: The ID of the HighDemandPeriod
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = HighDemandPeriod(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_highdemandperiod(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a HighDemandPeriod.

    Args:
        object_id: The ID of the HighDemandPeriod
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = HighDemandPeriod(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_highdemandperiod(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a HighDemandPeriod.

    Args:
        object_id: The ID of the HighDemandPeriod
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = HighDemandPeriod(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
highdemandperiod_server = mcp
