"""
Auto-generated MCP server for Facebook ShadowIGMediaCollaborators.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowigmediacollaborators import ShadowIGMediaCollaborators
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowigmediacollaborators")


# CRUD Operations


@mcp.tool()
async def api_create_shadowigmediacollaborators(
    shadowigmediacollaborators_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=shadowigmediacollaborators_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_shadowigmediacollaborators(
    shadowigmediacollaborators_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=shadowigmediacollaborators_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_shadowigmediacollaborators(
    shadowigmediacollaborators_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=shadowigmediacollaborators_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_shadowigmediacollaborators(
    shadowigmediacollaborators_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=shadowigmediacollaborators_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowigmediacollaborators_server = mcp
