"""
Auto-generated MCP server for Facebook EntityAtTextRange.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.entityattextrange import EntityAtTextRange
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-entityattextrange")


# CRUD Operations


@mcp.tool()
async def api_create_entityattextrange(
    entityattextrange_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EntityAtTextRange(fbid=entityattextrange_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_entityattextrange(
    entityattextrange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EntityAtTextRange(fbid=entityattextrange_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_entityattextrange(
    entityattextrange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EntityAtTextRange(fbid=entityattextrange_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_entityattextrange(
    entityattextrange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EntityAtTextRange(fbid=entityattextrange_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
entityattextrange_server = mcp
