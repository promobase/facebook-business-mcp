"""
Auto-generated MCP server for Facebook ProductFeedUploadError.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeeduploaderror import ProductFeedUploadError
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeeduploaderror")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    productfeeduploaderror_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_samples(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).get_samples(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_suggested_rules(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).get_suggested_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeeduploaderror_server = mcp
