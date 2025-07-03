"""
Auto-generated MCP server for Facebook AdsReportBuilderSavedReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildersavedreport import AdsReportBuilderSavedReport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildersavedreport")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adsreportbuildersavedreport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderSavedReport(fbid=adsreportbuildersavedreport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildersavedreport_server = mcp
