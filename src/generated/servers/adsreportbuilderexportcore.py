"""
Auto-generated MCP server for Facebook AdsReportBuilderExportCore.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuilderexportcore import AdsReportBuilderExportCore
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuilderexportcore")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adsreportbuilderexportcore_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuilderexportcore_server = mcp
