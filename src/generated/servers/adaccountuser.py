"""
Auto-generated MCP server for Facebook AdAccountUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountuser import AdAccountUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountuser")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountuser(
    adaccountuser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUser(fbid=adaccountuser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountuser(
    adaccountuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUser(fbid=adaccountuser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountuser(
    adaccountuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUser(fbid=adaccountuser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountuser(
    adaccountuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountUser(fbid=adaccountuser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountuser_server = mcp
