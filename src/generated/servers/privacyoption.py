"""
Auto-generated MCP server for Facebook PrivacyOption.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.privacyoption import PrivacyOption
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-privacyoption")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    privacyoption_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PrivacyOption(fbid=privacyoption_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PrivacyOption(fbid=privacyoption_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PrivacyOption(fbid=privacyoption_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PrivacyOption(fbid=privacyoption_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
privacyoption_server = mcp
