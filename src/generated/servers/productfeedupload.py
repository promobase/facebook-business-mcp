"""
Auto-generated MCP server for Facebook ProductFeedUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedupload import ProductFeedUpload
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedupload")


# CRUD Operations


@mcp.tool()
async def create_productfeedupload(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_error_report_for_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).create_error_report(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_errors_for_productfeedupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUpload(fbid=object_id).get_errors(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedupload_server = mcp
