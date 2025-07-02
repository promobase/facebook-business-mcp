"""
Auto-generated MCP server for Facebook CPASMerchantConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasmerchantconfig import CPASMerchantConfig
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasmerchantconfig")


# CRUD Operations


@mcp.tool()
async def api_create_cpasmerchantconfig(
    cpasmerchantconfig_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASMerchantConfig(fbid=cpasmerchantconfig_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_cpasmerchantconfig(
    cpasmerchantconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASMerchantConfig(fbid=cpasmerchantconfig_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_cpasmerchantconfig(
    cpasmerchantconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASMerchantConfig(fbid=cpasmerchantconfig_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_cpasmerchantconfig(
    cpasmerchantconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASMerchantConfig(fbid=cpasmerchantconfig_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasmerchantconfig_server = mcp
