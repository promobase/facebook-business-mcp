"""
Auto-generated MCP server for Facebook CustomAudiencesTOS.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customaudiencestos import CustomAudiencesTOS
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-customaudiencestos")


# CRUD Operations


@mcp.tool()
async def api_create_customaudiencestos(
    customaudiencestos_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudiencesTOS(fbid=customaudiencestos_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_customaudiencestos(
    customaudiencestos_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudiencesTOS(fbid=customaudiencestos_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_customaudiencestos(
    customaudiencestos_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudiencesTOS(fbid=customaudiencestos_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_customaudiencestos(
    customaudiencestos_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudiencesTOS(fbid=customaudiencestos_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customaudiencestos_server = mcp
