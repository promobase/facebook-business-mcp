"""Streamlined Campaign MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.generated.models.campaign import CampaignField, CampaignUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCampaign"
instructions = """
Campaign MCP Server for Facebook Business API.

Provides typed access to all Campaign operations.
"""

campaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_campaign(
    campaign_id: str,
    fields: list[CampaignField] = [],
) -> str:
    """Get a Campaign object by ID.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve.
    """
    obj = Campaign(campaign_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_campaign(
    campaign_id: str,
    fields: list[CampaignField] = [],
    params: CampaignUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a Campaign object.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return Campaign(campaign_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaign(
    campaign_id: str,
) -> str:
    """Delete a Campaign object.

    Args:
        campaign_id: The ID of the Campaign.
    """
    return Campaign(campaign_id).api_delete()


# ---- Edge Methods (9) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.campaign_wrappers import (
    create_ad_label,
    create_budget_schedule,
    create_copy,
    get_ad_rules_governed,
    get_ad_sets,
    get_ads,
    get_copies,
    get_insights,
    get_insights_async,
)

# ---- Register tools ----
# Register CRUD operations
campaign_server.tool(get_campaign)
campaign_server.tool(update_campaign)
campaign_server.tool(delete_campaign)

# Register edge methods from wrappers
campaign_server.tool(create_ad_label)
campaign_server.tool(get_ad_rules_governed)
campaign_server.tool(get_ads)
campaign_server.tool(get_ad_sets)
campaign_server.tool(create_budget_schedule)
campaign_server.tool(get_copies)
campaign_server.tool(create_copy)
campaign_server.tool(get_insights)
campaign_server.tool(get_insights_async)
