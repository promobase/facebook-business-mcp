"""
Auto-generated MCP server for Facebook ProductFeedUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedupload import ProductFeedUpload
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedupload")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    productfeedupload_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    productfeedupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    productfeedupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    productfeedupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_error_report(
    productfeedupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).create_error_report(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_errors(
    productfeedupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUpload(fbid=productfeedupload_id).get_errors(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedupload_server = mcp
