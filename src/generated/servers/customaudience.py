"""CustomAudience MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCustomAudience"
instructions = """
CustomAudience MCP Server for Facebook Business API.

Provides typed access to all CustomAudience operations.
"""

customaudience_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@customaudience_server.tool
@wrapped_fn_tool
def get_customaudience(
    customaudience_id: str,
    fields: list[str] = [],
) -> str:
    """Get a CustomAudience object by ID.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = CustomAudience(customaudience_id)
    return obj.api_get(fields=fields)


@customaudience_server.tool
@wrapped_fn_tool
def update_customaudience(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a CustomAudience object.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See CustomAudienceUpdateParams type.
    """
    return CustomAudience(customaudience_id).api_update(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def delete_customaudience(
    customaudience_id: str,
) -> str:
    """Delete a CustomAudience object.

    Args:
        customaudience_id: The ID of the CustomAudience.
    """
    return CustomAudience(customaudience_id).api_delete()


# ---- Edge Methods (11) ----
@customaudience_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    customaudience_id: str,
    params: dict = {},
):
    """Delete Ad Accounts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        params: Query parameters. Available params: See CustomAudienceDeleteAdAccountsParams type.
    """
    return CustomAudience(customaudience_id).delete_ad_accounts(params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_ad_accounts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ad Accounts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See CustomAudienceGetAdAccountsParams type.
    """
    return CustomAudience(customaudience_id).get_ad_accounts(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_ad_account(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Ad Account for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CustomAudienceCreateAdAccountParams type.
    """
    return CustomAudience(customaudience_id).create_ad_account(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_ads(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ads for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See CustomAudienceGetAdsParams type.
    """
    return CustomAudience(customaudience_id).get_ads(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_health(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Health for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See CustomAudienceHealthField type.
        params: Query parameters. Available params: See CustomAudienceGetHealthParams type.
    """
    return CustomAudience(customaudience_id).get_health(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_salts(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Salts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See CustomAudienceSaltsField type.
        params: Query parameters. Available params: See CustomAudienceGetSaltsParams type.
    """
    return CustomAudience(customaudience_id).get_salts(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_salt(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Salt for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CustomAudienceCreateSaltParams type.
    """
    return CustomAudience(customaudience_id).create_salt(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def get_sessions(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Sessions for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve. Available fields: See CustomAudienceSessionField type.
        params: Query parameters. Available params: See CustomAudienceGetSessionsParams type.
    """
    return CustomAudience(customaudience_id).get_sessions(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def delete_users(
    customaudience_id: str,
    params: dict = {},
):
    """Delete Users for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        params: Query parameters. Available params: See CustomAudienceDeleteUsersParams type.
    """
    return CustomAudience(customaudience_id).delete_users(params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_user(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create User for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CustomAudienceCreateUserParams type.
    """
    return CustomAudience(customaudience_id).create_user(fields=fields, params=params)


@customaudience_server.tool
@wrapped_fn_tool
def create_users_replace(
    customaudience_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Users Replace for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CustomAudienceCreateUsersReplaceParams type.
    """
    return CustomAudience(customaudience_id).create_users_replace(fields=fields, params=params)
