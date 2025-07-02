"""
Auto-generated MCP server for Facebook AdImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adimage import AdImage
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adimage")


# CRUD Operations


@mcp.tool()
async def api_create_adimage(
    adimage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdImage(fbid=adimage_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adimage(
    adimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdImage(fbid=adimage_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adimage(
    adimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdImage(fbid=adimage_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adimage(
    adimage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdImage(fbid=adimage_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adimage_server = mcp
