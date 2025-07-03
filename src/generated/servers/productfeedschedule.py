"""
Auto-generated MCP server for Facebook ProductFeedSchedule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedschedule import ProductFeedSchedule
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedschedule")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    productfeedschedule_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedSchedule(fbid=productfeedschedule_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    productfeedschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedSchedule(fbid=productfeedschedule_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    productfeedschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedSchedule(fbid=productfeedschedule_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    productfeedschedule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedSchedule(fbid=productfeedschedule_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedschedule_server = mcp
