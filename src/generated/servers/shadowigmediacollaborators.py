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
async def create_shadowigmediacollaborators(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_shadowigmediacollaborators(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shadowigmediacollaborators(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_shadowigmediacollaborators(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGMediaCollaborators(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowigmediacollaborators_server = mcp
