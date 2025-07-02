"""
Auto-generated MCP server for Facebook CustomAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi
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
    """
    Create a CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
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
    """
    Delete a CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
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
    """
    Get a CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Ad Account for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_account result
    """
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
    """
    Create Salt for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_salt result
    """
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
    """
    Create User for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_user result
    """
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
    """
    Create Users Replace for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_users_replace result
    """
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
    """
    Delete Ad Accounts for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_accounts result
    """
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
    """
    Delete Users for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_users result
    """
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
    """
    Get Ad Accounts for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
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
    """
    Get Ads for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads result
    """
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
    """
    Get Health for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_health result
    """
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
    """
    Get Salts for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_salts result
    """
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
    """
    Get Sessions for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sessions result
    """
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
    """
    Get Shared Account Info for CustomAudience.

    Args:
        object_id: The ID of the CustomAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_account_info result
    """
    result = CustomAudience(fbid=object_id).get_shared_account_info(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customaudience_server = mcp
