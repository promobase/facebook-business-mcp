"""
Auto-generated MCP server for Facebook AdPlacement.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adplacement import AdPlacement
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adplacement")


# CRUD Operations


@mcp.tool()
async def api_create_adplacement(
    adplacement_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacement(fbid=adplacement_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adplacement(
    adplacement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacement(fbid=adplacement_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adplacement(
    adplacement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacement(fbid=adplacement_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adplacement(
    adplacement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdPlacement(fbid=adplacement_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adplacement_server = mcp
