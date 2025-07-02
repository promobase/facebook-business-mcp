"""
Auto-generated MCP server for Facebook AdCustomDerivedMetrics.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcustomderivedmetrics import AdCustomDerivedMetrics
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcustomderivedmetrics")


# CRUD Operations


@mcp.tool()
async def api_create_adcustomderivedmetrics(
    adcustomderivedmetrics_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcustomderivedmetrics(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcustomderivedmetrics(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcustomderivedmetrics(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCustomDerivedMetrics(fbid=adcustomderivedmetrics_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcustomderivedmetrics_server = mcp
