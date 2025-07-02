"""
Auto-generated MCP server for Facebook AdKeywordStats.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adkeywordstats import AdKeywordStats
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adkeywordstats")


# CRUD Operations


@mcp.tool()
async def api_create_adkeywordstats(
    adkeywordstats_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdKeywordStats(fbid=adkeywordstats_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adkeywordstats(
    adkeywordstats_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdKeywordStats(fbid=adkeywordstats_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adkeywordstats(
    adkeywordstats_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdKeywordStats(fbid=adkeywordstats_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adkeywordstats(
    adkeywordstats_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdKeywordStats(fbid=adkeywordstats_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adkeywordstats_server = mcp
