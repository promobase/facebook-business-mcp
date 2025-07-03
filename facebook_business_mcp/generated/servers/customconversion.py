"""
Auto-generated MCP server for Facebook CustomConversion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customconversion import CustomConversion
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-customconversion")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    customconversion_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomConversion(fbid=customconversion_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomConversion(fbid=customconversion_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomConversion(fbid=customconversion_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomConversion(fbid=customconversion_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_stats(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomConversion(fbid=customconversion_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customconversion_server = mcp
