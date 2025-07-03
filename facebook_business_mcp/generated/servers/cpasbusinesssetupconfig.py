"""
Auto-generated MCP server for Facebook CPASBusinessSetupConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasbusinesssetupconfig import CPASBusinessSetupConfig
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasbusinesssetupconfig")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    cpasbusinesssetupconfig_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASBusinessSetupConfig(fbid=cpasbusinesssetupconfig_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    cpasbusinesssetupconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASBusinessSetupConfig(fbid=cpasbusinesssetupconfig_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    cpasbusinesssetupconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASBusinessSetupConfig(fbid=cpasbusinesssetupconfig_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    cpasbusinesssetupconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASBusinessSetupConfig(fbid=cpasbusinesssetupconfig_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    cpasbusinesssetupconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASBusinessSetupConfig(fbid=cpasbusinesssetupconfig_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasbusinesssetupconfig_server = mcp
