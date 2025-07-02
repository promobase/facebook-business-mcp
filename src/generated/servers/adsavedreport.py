"""
Auto-generated MCP server for Facebook AdSavedReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsavedreport import AdSavedReport
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsavedreport")


# CRUD Operations


@mcp.tool()
async def api_create_adsavedreport(
    adsavedreport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedReport(fbid=adsavedreport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsavedreport(
    adsavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedReport(fbid=adsavedreport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsavedreport(
    adsavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedReport(fbid=adsavedreport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsavedreport(
    adsavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedReport(fbid=adsavedreport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsavedreport_server = mcp
