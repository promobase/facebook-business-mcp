"""
Auto-generated MCP server for Facebook AdsPivotRules.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adspivotrules import AdsPivotRules
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adspivotrules")


# CRUD Operations


@mcp.tool()
async def api_create_adspivotrules(
    adspivotrules_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPivotRules(fbid=adspivotrules_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adspivotrules(
    adspivotrules_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPivotRules(fbid=adspivotrules_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adspivotrules(
    adspivotrules_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPivotRules(fbid=adspivotrules_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adspivotrules(
    adspivotrules_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsPivotRules(fbid=adspivotrules_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspivotrules_server = mcp
