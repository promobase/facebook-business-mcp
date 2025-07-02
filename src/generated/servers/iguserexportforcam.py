"""
Auto-generated MCP server for Facebook IGUserExportForCAM.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguserexportforcam import IGUserExportForCAM
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguserexportforcam")


# CRUD Operations


@mcp.tool()
async def create_iguserexportforcam(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_branded_content_media_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).get_branded_content_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recent_media_for_iguserexportforcam(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=object_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserexportforcam_server = mcp
