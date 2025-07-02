"""
Auto-generated MCP server for Facebook AdsConversionGoal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsconversiongoal import AdsConversionGoal
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsconversiongoal")


# CRUD Operations


@mcp.tool()
async def create_adsconversiongoal(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsConversionGoal(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsConversionGoal(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsConversionGoal(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsConversionGoal(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_conversion_events_for_adsconversiongoal(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsConversionGoal(fbid=object_id).get_conversion_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsconversiongoal_server = mcp
