"""
Auto-generated MCP server for Facebook CustomAudienceAdAccount.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customaudienceadaccount import CustomAudienceAdAccount
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-customaudienceadaccount")


# CRUD Operations


@mcp.tool()
async def api_create_customaudienceadaccount(
    customaudienceadaccount_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudienceAdAccount(fbid=customaudienceadaccount_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_customaudienceadaccount(
    customaudienceadaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudienceAdAccount(fbid=customaudienceadaccount_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_customaudienceadaccount(
    customaudienceadaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudienceAdAccount(fbid=customaudienceadaccount_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_customaudienceadaccount(
    customaudienceadaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudienceAdAccount(fbid=customaudienceadaccount_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customaudienceadaccount_server = mcp
