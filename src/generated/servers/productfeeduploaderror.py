"""
Auto-generated MCP server for Facebook ProductFeedUploadError.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeeduploaderror import ProductFeedUploadError
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeeduploaderror")


# CRUD Operations


@mcp.tool()
async def api_create_productfeeduploaderror(
    productfeeduploaderror_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_productfeeduploaderror(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_productfeeduploaderror(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_productfeeduploaderror(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_samples(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).get_samples(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_suggested_rules(
    productfeeduploaderror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=productfeeduploaderror_id).get_suggested_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeeduploaderror_server = mcp
