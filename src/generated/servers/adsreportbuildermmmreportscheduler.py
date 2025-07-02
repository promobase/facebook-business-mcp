"""
Auto-generated MCP server for Facebook AdsReportBuilderMMMReportScheduler.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildermmmreportscheduler import (
    AdsReportBuilderMMMReportScheduler,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildermmmreportscheduler")


# CRUD Operations


@mcp.tool()
async def api_create_adsreportbuildermmmreportscheduler(
    adsreportbuildermmmreportscheduler_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReportScheduler(
        fbid=adsreportbuildermmmreportscheduler_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsreportbuildermmmreportscheduler(
    adsreportbuildermmmreportscheduler_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReportScheduler(
        fbid=adsreportbuildermmmreportscheduler_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsreportbuildermmmreportscheduler(
    adsreportbuildermmmreportscheduler_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReportScheduler(fbid=adsreportbuildermmmreportscheduler_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsreportbuildermmmreportscheduler(
    adsreportbuildermmmreportscheduler_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderMMMReportScheduler(
        fbid=adsreportbuildermmmreportscheduler_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildermmmreportscheduler_server = mcp
