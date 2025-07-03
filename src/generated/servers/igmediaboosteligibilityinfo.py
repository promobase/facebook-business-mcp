"""
Auto-generated MCP server for Facebook IGMediaBoostEligibilityInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaboosteligibilityinfo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    igmediaboosteligibilityinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    igmediaboosteligibilityinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaBoostEligibilityInfo(fbid=igmediaboosteligibilityinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaboosteligibilityinfo_server = mcp
