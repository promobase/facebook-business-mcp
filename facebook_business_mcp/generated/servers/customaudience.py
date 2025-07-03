"""
Auto-generated MCP server for Facebook CustomAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-customaudience")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    customaudience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_ad_account(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_salt(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).create_salt(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_user(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).create_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_users_replace(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).create_users_replace(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_ad_accounts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_users(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).delete_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ads(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_health(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_health(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_salts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_salts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_sessions(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_sessions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_account_info(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CustomAudience(fbid=customaudience_id).get_shared_account_info(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customaudience_server = mcp
