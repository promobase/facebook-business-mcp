"""Streamlined AdSet MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.generated.models.adset import AdSetField, AdSetUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSet"
instructions = """
AdSet MCP Server for Facebook Business API.

Provides typed access to all AdSet operations.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[AdSetField] = [],
) -> str:
    """Get a AdSet object by ID.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
    """
    obj = AdSet(adset_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[AdSetField] = [],
    params: AdSetUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdSet(adset_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_adset(
    adset_id: str,
) -> str:
    """Delete a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
    """
    return AdSet(adset_id).api_delete()


# ---- Edge Methods (13) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.adset_wrappers import (
    create_ad_label,
    create_budget_schedule,
    create_copy,
    delete_ad_labels,
    get_activities,
    get_ad_rules_governed,
    get_ads,
    get_async_ad_requests,
    get_copies,
    get_delivery_estimate,
    get_insights,
    get_insights_async,
    get_message_delivery_estimate,
)

# ---- Register tools ----
# Register CRUD operations
adset_server.tool(get_adset)
adset_server.tool(update_adset)
adset_server.tool(delete_adset)

# Register edge methods from wrappers
adset_server.tool(get_activities)
adset_server.tool(delete_ad_labels)
adset_server.tool(create_ad_label)
adset_server.tool(get_ad_rules_governed)
adset_server.tool(get_ads)
adset_server.tool(get_async_ad_requests)
adset_server.tool(create_budget_schedule)
adset_server.tool(get_copies)
adset_server.tool(create_copy)
adset_server.tool(get_delivery_estimate)
adset_server.tool(get_insights)
adset_server.tool(get_insights_async)
adset_server.tool(get_message_delivery_estimate)
