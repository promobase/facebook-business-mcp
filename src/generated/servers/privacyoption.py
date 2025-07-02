"""
Auto-generated MCP server for Facebook PrivacyOption.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.privacyoption import PrivacyOption
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-privacyoption")


# CRUD Operations


@mcp.tool()
async def api_create_privacyoption(
    privacyoption_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivacyOption(fbid=privacyoption_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_privacyoption(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivacyOption(fbid=privacyoption_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_privacyoption(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivacyOption(fbid=privacyoption_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_privacyoption(
    privacyoption_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PrivacyOption(fbid=privacyoption_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
privacyoption_server = mcp
