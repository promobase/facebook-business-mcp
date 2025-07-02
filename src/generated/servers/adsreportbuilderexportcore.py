"""
Auto-generated MCP server for Facebook AdsReportBuilderExportCore.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuilderexportcore import AdsReportBuilderExportCore
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuilderexportcore")


# CRUD Operations


@mcp.tool()
async def api_create_adsreportbuilderexportcore(
    adsreportbuilderexportcore_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsreportbuilderexportcore(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsreportbuilderexportcore(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsreportbuilderexportcore(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsReportBuilderExportCore(fbid=adsreportbuilderexportcore_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuilderexportcore_server = mcp
