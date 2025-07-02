"""
Auto-generated MCP server for Facebook AREffect.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.areffect import AREffect
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-areffect")


# CRUD Operations


@mcp.tool()
async def api_create_areffect(
    areffect_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AREffect(fbid=areffect_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_areffect(
    areffect_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AREffect(fbid=areffect_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_areffect(
    areffect_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AREffect(fbid=areffect_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_areffect(
    areffect_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AREffect(fbid=areffect_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
areffect_server = mcp
