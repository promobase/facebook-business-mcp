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
async def create_automotivemodel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AutomotiveModel(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
automotivemodel_server = mcp
