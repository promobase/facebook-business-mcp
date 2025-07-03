"""
Auto-generated MCP server for Facebook SocialWifiSite.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.socialwifisite import SocialWifiSite
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-socialwifisite")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    socialwifisite_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SocialWifiSite(fbid=socialwifisite_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SocialWifiSite(fbid=socialwifisite_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SocialWifiSite(fbid=socialwifisite_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SocialWifiSite(fbid=socialwifisite_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
socialwifisite_server = mcp
