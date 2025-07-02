"""
Auto-generated MCP server for Facebook AdAssetTitle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassettitle import AdAssetTitle
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassettitle")


# CRUD Operations


@mcp.tool()
async def api_create_adassettitle(
    adassettitle_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetTitle(fbid=adassettitle_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassettitle(
    adassettitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetTitle(fbid=adassettitle_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassettitle(
    adassettitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetTitle(fbid=adassettitle_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassettitle(
    adassettitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetTitle(fbid=adassettitle_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassettitle_server = mcp
