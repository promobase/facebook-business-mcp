"""
Auto-generated MCP server for Facebook AutomotiveModel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.automotivemodel import AutomotiveModel
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-automotivemodel")


# CRUD Operations


@mcp.tool()
async def api_create_automotivemodel(
    automotivemodel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_automotivemodel(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_automotivemodel(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_automotivemodel(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=automotivemodel_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
automotivemodel_server = mcp
