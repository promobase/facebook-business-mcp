"""
Auto-generated MCP server for Facebook DynamicPriceConfigByDate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicpriceconfigbydate import DynamicPriceConfigByDate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicpriceconfigbydate")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    dynamicpriceconfigbydate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicPriceConfigByDate(fbid=dynamicpriceconfigbydate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    dynamicpriceconfigbydate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicPriceConfigByDate(fbid=dynamicpriceconfigbydate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    dynamicpriceconfigbydate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicPriceConfigByDate(fbid=dynamicpriceconfigbydate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    dynamicpriceconfigbydate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicPriceConfigByDate(fbid=dynamicpriceconfigbydate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicpriceconfigbydate_server = mcp
