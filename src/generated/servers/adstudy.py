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
async def create_adstudy(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_check_point_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).create_check_point(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_instance_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).create_instance(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cells_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).get_cells(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instances_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).get_instances(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_objectives_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdStudy(fbid=object_id).get_objectives(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudy_server = mcp
