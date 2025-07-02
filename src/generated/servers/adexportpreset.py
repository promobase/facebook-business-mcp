"""
Auto-generated MCP server for Facebook AdExportPreset.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adexportpreset import AdExportPreset
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adexportpreset")


# CRUD Operations


@mcp.tool()
async def api_create_adexportpreset(
    adexportpreset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdExportPreset(fbid=adexportpreset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adexportpreset(
    adexportpreset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdExportPreset(fbid=adexportpreset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adexportpreset(
    adexportpreset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdExportPreset(fbid=adexportpreset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adexportpreset(
    adexportpreset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdExportPreset(fbid=adexportpreset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adexportpreset_server = mcp
