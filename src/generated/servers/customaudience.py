"""
Auto-generated MCP server for Facebook CustomAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-customaudience")


# CRUD Operations


@mcp.tool()
async def create_customaudience(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_account_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).create_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_salt_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).create_salt(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_user_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).create_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_users_replace_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).create_users_replace(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_accounts_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).delete_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_users_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).delete_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_health_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_health(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_salts_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_salts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sessions_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_sessions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_account_info_for_customaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CustomAudience(fbid=object_id).get_shared_account_info(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customaudience_server = mcp
