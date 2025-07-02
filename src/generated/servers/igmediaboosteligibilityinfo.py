"""
Auto-generated MCP server for Facebook IGMediaBoostEligibilityInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaboosteligibilityinfo")


# CRUD Operations


@mcp.tool()
async def api_create_igmediaboosteligibilityinfo(
    igmediaboosteligibilityinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igmediaboosteligibilityinfo(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igmediaboosteligibilityinfo(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igmediaboosteligibilityinfo(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaboosteligibilityinfo_server = mcp
