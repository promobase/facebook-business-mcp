"""
Auto-generated MCP server for Facebook SiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.sitelink import SiteLink
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-sitelink")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    sitelink_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SiteLink(fbid=sitelink_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SiteLink(fbid=sitelink_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SiteLink(fbid=sitelink_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SiteLink(fbid=sitelink_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
sitelink_server = mcp
