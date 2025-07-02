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
async def create_productfeeduploaderror(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_samples_for_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).get_samples(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_suggested_rules_for_productfeeduploaderror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductFeedUploadError(fbid=object_id).get_suggested_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeeduploaderror_server = mcp
