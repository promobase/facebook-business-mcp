"""
Auto-generated MCP server for Facebook AdLightAdgroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adlightadgroup import AdLightAdgroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adlightadgroup")


# CRUD Operations


@mcp.tool()
async def api_create_adlightadgroup(
    adlightadgroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightAdgroup(fbid=adlightadgroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adlightadgroup(
    adlightadgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightAdgroup(fbid=adlightadgroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adlightadgroup(
    adlightadgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightAdgroup(fbid=adlightadgroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adlightadgroup(
    adlightadgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdLightAdgroup(fbid=adlightadgroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adlightadgroup_server = mcp
