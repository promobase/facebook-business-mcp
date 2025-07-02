"""
Auto-generated MCP server for Facebook PartnerStudy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partnerstudy import PartnerStudy
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-partnerstudy")


# CRUD Operations


@mcp.tool()
async def api_create_partnerstudy(
    partnerstudy_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerStudy(fbid=partnerstudy_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_partnerstudy(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerStudy(fbid=partnerstudy_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_partnerstudy(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerStudy(fbid=partnerstudy_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_partnerstudy(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PartnerStudy(fbid=partnerstudy_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partnerstudy_server = mcp
