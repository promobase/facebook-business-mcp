"""
Auto-generated MCP server for Facebook PageInsightsAsyncExportRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageinsightsasyncexportrun import PageInsightsAsyncExportRun
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageinsightsasyncexportrun")


# CRUD Operations


@mcp.tool()
async def api_create_pageinsightsasyncexportrun(
    pageinsightsasyncexportrun_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageInsightsAsyncExportRun(fbid=pageinsightsasyncexportrun_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pageinsightsasyncexportrun(
    pageinsightsasyncexportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageInsightsAsyncExportRun(fbid=pageinsightsasyncexportrun_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pageinsightsasyncexportrun(
    pageinsightsasyncexportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageInsightsAsyncExportRun(fbid=pageinsightsasyncexportrun_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pageinsightsasyncexportrun(
    pageinsightsasyncexportrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageInsightsAsyncExportRun(fbid=pageinsightsasyncexportrun_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageinsightsasyncexportrun_server = mcp
