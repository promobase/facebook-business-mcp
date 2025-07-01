"""Streamlined CustomAudience MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.customaudience import CustomAudience
from fastmcp import FastMCP

from src.generated.models.customaudience import CustomAudienceField, CustomAudienceUpdateParams
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
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.customaudience_wrappers import (
    create_ad_account,
    create_salt,
    create_user,
    create_users_replace,
    delete_ad_accounts,
    delete_users,
    get_ad_accounts,
    get_ads,
    get_health,
    get_salts,
    get_sessions,
)

# ---- Register tools ----
# Register CRUD operations
customaudience_server.tool(get_customaudience)
customaudience_server.tool(update_customaudience)
customaudience_server.tool(delete_customaudience)

# Register edge methods from wrappers
customaudience_server.tool(delete_ad_accounts)
customaudience_server.tool(get_ad_accounts)
customaudience_server.tool(create_ad_account)
customaudience_server.tool(get_ads)
customaudience_server.tool(get_health)
customaudience_server.tool(get_salts)
customaudience_server.tool(create_salt)
customaudience_server.tool(get_sessions)
customaudience_server.tool(delete_users)
customaudience_server.tool(create_user)
customaudience_server.tool(create_users_replace)
