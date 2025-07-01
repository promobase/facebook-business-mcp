"""Streamlined AdsPixel MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

from src.generated.models.adspixel import AdsPixelField, AdsPixelUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPixel"
instructions = """
AdsPixel MCP Server for Facebook Business API.

Provides typed access to all AdsPixel operations.
"""

adspixel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@wrapped_fn_tool
def get_adspixel(
    adspixel_id: str,
    fields: list[AdsPixelField] = [],
) -> str:
    """Get a AdsPixel object by ID.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
    """
    obj = AdsPixel(adspixel_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_adspixel(
    adspixel_id: str,
    fields: list[AdsPixelField] = [],
    params: AdsPixelUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdsPixel object.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdsPixel(adspixel_id).api_update(fields=fields, params=params)


# ---- Edge Methods (13) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.adspixel_wrappers import (
    create_agency,
    create_ahp_config,
    create_assigned_user,
    create_event,
    create_shared_account,
    delete_agencies,
    delete_shared_accounts,
    get_ad_accounts,
    get_assigned_users,
    get_da_checks,
    get_offline_event_uploads,
    get_shared_accounts,
    get_stats,
)

# ---- Register tools ----
# Register CRUD operations
adspixel_server.tool(get_adspixel)
adspixel_server.tool(update_adspixel)

# Register edge methods from wrappers
adspixel_server.tool(get_ad_accounts)
adspixel_server.tool(delete_agencies)
adspixel_server.tool(create_agency)
adspixel_server.tool(create_ahp_config)
adspixel_server.tool(get_assigned_users)
adspixel_server.tool(create_assigned_user)
adspixel_server.tool(get_da_checks)
adspixel_server.tool(create_event)
adspixel_server.tool(get_offline_event_uploads)
adspixel_server.tool(delete_shared_accounts)
adspixel_server.tool(get_shared_accounts)
adspixel_server.tool(create_shared_account)
adspixel_server.tool(get_stats)
