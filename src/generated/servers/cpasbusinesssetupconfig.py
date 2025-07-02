"""
Auto-generated MCP server for Facebook CPASBusinessSetupConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasbusinesssetupconfig import CPASBusinessSetupConfig
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasbusinesssetupconfig")


# CRUD Operations


@mcp.tool()
async def create_cpasbusinesssetupconfig(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASBusinessSetupConfig(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASBusinessSetupConfig(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASBusinessSetupConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASBusinessSetupConfig(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_cpasbusinesssetupconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASBusinessSetupConfig(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasbusinesssetupconfig_server = mcp
