"""CustomAudience MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

from src.generated.models.ad import AdField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.customaudience import (
    CustomAudienceCreateAdAccountParams,
    CustomAudienceCreateSaltParams,
    CustomAudienceCreateUserParams,
    CustomAudienceCreateUsersReplaceParams,
    CustomAudienceDeleteAdAccountsParams,
    CustomAudienceDeleteUsersParams,
    CustomAudienceField,
    CustomAudienceGetAdAccountsParams,
    CustomAudienceGetAdsParams,
    CustomAudienceGetHealthParams,
    CustomAudienceGetSaltsParams,
    CustomAudienceGetSessionsParams,
    CustomAudienceUpdateParams,
)
from src.generated.models.customaudiencehealth import CustomAudienceHealthField
from src.generated.models.customaudiencesalts import CustomAudienceSaltsField
from src.generated.models.customaudiencesession import CustomAudienceSessionField
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
@wrapped_fn_tool
def get_customaudience(
    customaudience_id: str,
    fields: list[CustomAudienceField] = [],
) -> str:
    """Get a CustomAudience object by ID.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
    """
    obj = CustomAudience(customaudience_id)
    return obj.api_get(fields=fields)


customaudience_server.tool(get_customaudience)


@wrapped_fn_tool
def update_customaudience(
    customaudience_id: str,
    fields: list[CustomAudienceField] = [],
    params: CustomAudienceUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a CustomAudience object.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return CustomAudience(customaudience_id).api_update(fields=fields, params=params)


customaudience_server.tool(update_customaudience)


@wrapped_fn_tool
def delete_customaudience(
    customaudience_id: str,
) -> str:
    """Delete a CustomAudience object.

    Args:
        customaudience_id: The ID of the CustomAudience.
    """
    return CustomAudience(customaudience_id).api_delete()


customaudience_server.tool(delete_customaudience)


# ---- Edge Methods (11) ----
@wrapped_fn_tool
def delete_ad_accounts(
    customaudience_id: str,
    params: CustomAudienceDeleteAdAccountsParams = {},
) -> Any:
    """Delete Ad Accounts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).delete_ad_accounts(params=params)


customaudience_server.tool(delete_ad_accounts)


@wrapped_fn_tool
def get_ad_accounts(
    customaudience_id: str,
    fields: list[AdAccountField] = [],
    params: CustomAudienceGetAdAccountsParams = {},
) -> Any:
    """Get Ad Accounts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).get_ad_accounts(fields=fields, params=params)


customaudience_server.tool(get_ad_accounts)


@wrapped_fn_tool
def create_ad_account(
    customaudience_id: str,
    fields: list[str] = [],
    params: CustomAudienceCreateAdAccountParams = {},
) -> Any:
    """Create Ad Account for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).create_ad_account(fields=fields, params=params)


customaudience_server.tool(create_ad_account)


@wrapped_fn_tool
def get_ads(
    customaudience_id: str,
    fields: list[AdField] = [],
    params: CustomAudienceGetAdsParams = {},
) -> Any:
    """Get Ads for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).get_ads(fields=fields, params=params)


customaudience_server.tool(get_ads)


@wrapped_fn_tool
def get_health(
    customaudience_id: str,
    fields: list[CustomAudienceHealthField] = [],
    params: CustomAudienceGetHealthParams = {},
) -> Any:
    """Get Health for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).get_health(fields=fields, params=params)


customaudience_server.tool(get_health)


@wrapped_fn_tool
def get_salts(
    customaudience_id: str,
    fields: list[CustomAudienceSaltsField] = [],
    params: CustomAudienceGetSaltsParams = {},
) -> Any:
    """Get Salts for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).get_salts(fields=fields, params=params)


customaudience_server.tool(get_salts)


@wrapped_fn_tool
def create_salt(
    customaudience_id: str,
    fields: list[str] = [],
    params: CustomAudienceCreateSaltParams = {},
) -> Any:
    """Create Salt for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).create_salt(fields=fields, params=params)


customaudience_server.tool(create_salt)


@wrapped_fn_tool
def get_sessions(
    customaudience_id: str,
    fields: list[CustomAudienceSessionField] = [],
    params: CustomAudienceGetSessionsParams = {},
) -> Any:
    """Get Sessions for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).get_sessions(fields=fields, params=params)


customaudience_server.tool(get_sessions)


@wrapped_fn_tool
def delete_users(
    customaudience_id: str,
    params: CustomAudienceDeleteUsersParams = {},
) -> Any:
    """Delete Users for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).delete_users(params=params)


customaudience_server.tool(delete_users)


@wrapped_fn_tool
def create_user(
    customaudience_id: str,
    fields: list[str] = [],
    params: CustomAudienceCreateUserParams = {},
) -> Any:
    """Create User for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).create_user(fields=fields, params=params)


customaudience_server.tool(create_user)


@wrapped_fn_tool
def create_users_replace(
    customaudience_id: str,
    fields: list[str] = [],
    params: CustomAudienceCreateUsersReplaceParams = {},
) -> Any:
    """Create Users Replace for this CustomAudience.

    Args:
        customaudience_id: The ID of the CustomAudience.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return CustomAudience(customaudience_id).create_users_replace(fields=fields, params=params)


customaudience_server.tool(create_users_replace)
