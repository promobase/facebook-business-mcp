"""
Auto-generated MCP server for Facebook ImageCopyrightDispute.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.imagecopyrightdispute import ImageCopyrightDispute
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-imagecopyrightdispute")


# CRUD Operations


@mcp.tool()
async def api_create_imagecopyrightdispute(
    imagecopyrightdispute_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ImageCopyrightDispute(fbid=imagecopyrightdispute_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_imagecopyrightdispute(
    imagecopyrightdispute_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ImageCopyrightDispute(fbid=imagecopyrightdispute_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_imagecopyrightdispute(
    imagecopyrightdispute_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ImageCopyrightDispute(fbid=imagecopyrightdispute_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_imagecopyrightdispute(
    imagecopyrightdispute_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ImageCopyrightDispute(fbid=imagecopyrightdispute_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
imagecopyrightdispute_server = mcp
