"""
Auto-generated MCP server for Facebook InstagramRelatedProductTags.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramrelatedproducttags import InstagramRelatedProductTags
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramrelatedproducttags")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    instagramrelatedproducttags_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramRelatedProductTags(fbid=instagramrelatedproducttags_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    instagramrelatedproducttags_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramRelatedProductTags(fbid=instagramrelatedproducttags_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    instagramrelatedproducttags_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramRelatedProductTags(fbid=instagramrelatedproducttags_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    instagramrelatedproducttags_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramRelatedProductTags(fbid=instagramrelatedproducttags_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramrelatedproducttags_server = mcp
