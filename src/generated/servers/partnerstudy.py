"""
Auto-generated MCP server for Facebook PartnerStudy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.partnerstudy import PartnerStudy
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-partnerstudy")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    partnerstudy_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PartnerStudy(fbid=partnerstudy_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PartnerStudy(fbid=partnerstudy_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PartnerStudy(fbid=partnerstudy_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    partnerstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PartnerStudy(fbid=partnerstudy_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
partnerstudy_server = mcp
