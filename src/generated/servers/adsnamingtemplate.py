"""
Auto-generated MCP server for Facebook AdsNamingTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsnamingtemplate import AdsNamingTemplate
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsnamingtemplate")


# CRUD Operations


@mcp.tool()
async def api_create_adsnamingtemplate(
    adsnamingtemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsNamingTemplate(fbid=adsnamingtemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsnamingtemplate(
    adsnamingtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsNamingTemplate(fbid=adsnamingtemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsnamingtemplate(
    adsnamingtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsNamingTemplate(fbid=adsnamingtemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsnamingtemplate(
    adsnamingtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsNamingTemplate(fbid=adsnamingtemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsnamingtemplate_server = mcp
