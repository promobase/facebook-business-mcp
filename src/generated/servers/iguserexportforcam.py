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
async def api_create_iguserexportforcam(
    iguserexportforcam_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_iguserexportforcam(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_iguserexportforcam(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_iguserexportforcam(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_branded_content_media(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).get_branded_content_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recent_media(
    iguserexportforcam_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserExportForCAM(fbid=iguserexportforcam_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserexportforcam_server = mcp
