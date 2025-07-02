"""
Auto-generated MCP server for Facebook AdsReportBuilderSavedReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildersavedreport import AdsReportBuilderSavedReport
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildersavedreport")


# CRUD Operations


@mcp.tool()
async def api_create_adsreportbuildersavedreport(
    adsreportbuildersavedreport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsreportbuildersavedreport(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsreportbuildersavedreport(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsreportbuildersavedreport(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildersavedreport_server = mcp
