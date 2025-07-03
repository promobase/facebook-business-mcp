"""
Auto-generated MCP server for Facebook AdReportRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adreportrun import AdReportRun
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adreportrun")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adreportrun_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdReportRun(fbid=adreportrun_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adreportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdReportRun(fbid=adreportrun_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adreportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdReportRun(fbid=adreportrun_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adreportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdReportRun(fbid=adreportrun_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    adreportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdReportRun(fbid=adreportrun_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adreportrun_server = mcp
