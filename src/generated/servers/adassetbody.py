"""
Auto-generated MCP server for Facebook AdAssetBody.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetbody import AdAssetBody
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetbody")


# CRUD Operations


@mcp.tool()
async def api_create_adassetbody(
    adassetbody_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetBody(fbid=adassetbody_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassetbody(
    adassetbody_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetBody(fbid=adassetbody_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassetbody(
    adassetbody_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetBody(fbid=adassetbody_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassetbody(
    adassetbody_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetBody(fbid=adassetbody_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetbody_server = mcp
