"""
Auto-generated MCP server for Facebook AdsTargetingInsights.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstargetinginsights import AdsTargetingInsights
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstargetinginsights")


# CRUD Operations


@mcp.tool()
async def api_create_adstargetinginsights(
    adstargetinginsights_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsTargetingInsights(fbid=adstargetinginsights_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adstargetinginsights(
    adstargetinginsights_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsTargetingInsights(fbid=adstargetinginsights_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adstargetinginsights(
    adstargetinginsights_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsTargetingInsights(fbid=adstargetinginsights_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adstargetinginsights(
    adstargetinginsights_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsTargetingInsights(fbid=adstargetinginsights_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstargetinginsights_server = mcp
