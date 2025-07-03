"""
Auto-generated MCP server for Facebook AdsReportBuilderMMMReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildermmmreport import AdsReportBuilderMMMReport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildermmmreport")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adsreportbuildermmmreport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderMMMReport(fbid=adsreportbuildermmmreport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildermmmreport_server = mcp
