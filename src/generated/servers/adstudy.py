"""
Auto-generated MCP server for Facebook AdStudy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudy import AdStudy
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudy")


# CRUD Operations


@mcp.tool()
async def api_create_adstudy(
    adstudy_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adstudy(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adstudy(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adstudy(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_check_point(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).create_check_point(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_instance(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).create_instance(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cells(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).get_cells(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instances(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).get_instances(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_objectives(
    adstudy_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=adstudy_id).get_objectives(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudy_server = mcp
