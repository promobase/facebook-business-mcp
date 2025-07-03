"""
Auto-generated MCP server for Facebook InstagramInsightsResult.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagraminsightsresult import InstagramInsightsResult
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-instagraminsightsresult")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    instagraminsightsresult_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramInsightsResult(fbid=instagraminsightsresult_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    instagraminsightsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramInsightsResult(fbid=instagraminsightsresult_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    instagraminsightsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramInsightsResult(fbid=instagraminsightsresult_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    instagraminsightsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = InstagramInsightsResult(fbid=instagraminsightsresult_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagraminsightsresult_server = mcp
