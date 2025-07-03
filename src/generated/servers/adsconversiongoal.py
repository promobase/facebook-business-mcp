"""
Auto-generated MCP server for Facebook AdsConversionGoal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsconversiongoal import AdsConversionGoal
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adsconversiongoal")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adsconversiongoal_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsConversionGoal(fbid=adsconversiongoal_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adsconversiongoal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsConversionGoal(fbid=adsconversiongoal_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adsconversiongoal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsConversionGoal(fbid=adsconversiongoal_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adsconversiongoal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsConversionGoal(fbid=adsconversiongoal_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_conversion_events(
    adsconversiongoal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsConversionGoal(fbid=adsconversiongoal_id).get_conversion_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsconversiongoal_server = mcp
