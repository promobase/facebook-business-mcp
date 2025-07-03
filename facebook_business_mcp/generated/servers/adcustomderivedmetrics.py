"""
Auto-generated MCP server for Facebook AdCustomDerivedMetrics.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcustomderivedmetrics import AdCustomDerivedMetrics
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adcustomderivedmetrics")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adcustomderivedmetrics_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcustomderivedmetrics_server = mcp
