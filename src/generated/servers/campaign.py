"""Campaign MCP Server."""

from typing import Any

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

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
@campaign_server.tool
@wrapped_fn_tool
def get_campaign(
    campaign_id: str,
    fields: list[str] = [],
) -> str:
    obj = Campaign(campaign_id)
    return obj.api_get(fields=fields)


@campaign_server.tool
@wrapped_fn_tool
def update_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).api_update(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def delete_campaign(
    campaign_id: str,
) -> str:
    return Campaign(campaign_id).api_delete()


# ---- Edge Methods (9) ----
@campaign_server.tool
@wrapped_fn_tool
def create_ad_label(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).create_ad_label(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ad_rules_governed(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_ad_rules_governed(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ads(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_ads(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ad_sets(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_ad_sets(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def create_budget_schedule(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).create_budget_schedule(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_copies(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_copies(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def create_copy(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).create_copy(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_insights(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_insights(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_insights_async(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Campaign(campaign_id).get_insights_async(fields=fields, params=params)
