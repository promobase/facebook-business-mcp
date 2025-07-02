"""
Auto-generated MCP server for Facebook AdsReportBuilderMMMReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildermmmreport import AdsReportBuilderMMMReport
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildermmmreport")


# CRUD Operations


@mcp.tool()
async def api_create_adsreportbuildermmmreport(
    adsreportbuildermmmreport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsreportbuildermmmreport(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsreportbuildermmmreport(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsreportbuildermmmreport(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildermmmreport_server = mcp
