"""
Auto-generated MCP server for Facebook HighDemandPeriod.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.highdemandperiod import HighDemandPeriod
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-highdemandperiod")


# CRUD Operations


@mcp.tool()
async def api_create_highdemandperiod(
    highdemandperiod_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = HighDemandPeriod(fbid=highdemandperiod_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = HighDemandPeriod(fbid=highdemandperiod_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = HighDemandPeriod(fbid=highdemandperiod_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = HighDemandPeriod(fbid=highdemandperiod_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
highdemandperiod_server = mcp
