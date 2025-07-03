"""Campaign CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook campaigns.
"""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.generated.models import AdAccountField
from facebook_business_mcp.utils import handle_facebook_errors, use_adaccount_id, wrapped_fn_tool


class CommonCampaignFields:
    """
    A class to hold common sets of fields for Facebook Ad Campaigns.
    Fields are grouped by estimated usage frequency.
    """

    # --- High-Frequency Fields ---
    # Essential fields for most reports and basic identification.
    high_frequency = [
        Campaign.Field.id,
        Campaign.Field.name,
        Campaign.Field.status,
        Campaign.Field.effective_status,
        Campaign.Field.objective,
        Campaign.Field.daily_budget,
        Campaign.Field.lifetime_budget,
    ]

    # --- Medium-Frequency Fields ---
    # Important for detailed analysis, performance tracking, and debugging.
    medium_frequency = [
        Campaign.Field.start_time,
        Campaign.Field.stop_time,
        Campaign.Field.created_time,
        Campaign.Field.updated_time,
        Campaign.Field.buying_type,
        Campaign.Field.spend_cap,
        Campaign.Field.budget_remaining,
        Campaign.Field.adlabels,
        Campaign.Field.issues_info,
    ]

    # --- Low-Frequency Fields ---
    # Specialized fields for specific campaign types or advanced auditing.
    low_frequency = [
        Campaign.Field.account_id,
        Campaign.Field.boosted_object_id,
        Campaign.Field.brand_lift_studies,
        Campaign.Field.can_use_spend_cap,
        Campaign.Field.configured_status,
        Campaign.Field.pacing_type,
        Campaign.Field.promoted_object,
        Campaign.Field.source_campaign_id,
        Campaign.Field.special_ad_categories,
        Campaign.Field.bid_strategy,
        Campaign.Field.recommendations,
    ]

    # --- Combined 'basic' list ---
    # A practical default for general queries, combining high and medium frequency fields.
    basic = list(set(high_frequency + medium_frequency))


@wrapped_fn_tool
def adaccount_get_campaigns(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad campaigns of an ad account. If no fields, we will use basic fields for most frequent fields access."""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    if not fields:
        fields = CommonCampaignFields.basic
    return ad_account.get_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def adaccount_delete_campaigns(
    adaccount_id: str,
    params: dict[str, Any] = {},
) -> bool:
    """delete campaigns from an ad account."""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.delete_campaigns(params=params)


@wrapped_fn_tool
def campaign_api_get(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get a campaign by ID."""
    campaign = Campaign(campaign_id)
    return campaign.api_get(fields=fields, params=params)


@wrapped_fn_tool
def campaign_api_create(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """create a campaign from an ad account."""
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    account = AdAccount(account_id)
    return account.create_campaign(fields=fields, params=params)


@wrapped_fn_tool
def campaign_api_update(
    campaign_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update a campaign"""

    campaign = Campaign(campaign_id)
    return campaign.api_update(fields=fields, params=params)


@wrapped_fn_tool
def campaign_api_delete(campaign_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete a campaign"""
    campaign = Campaign(campaign_id)
    return campaign.api_delete(params=params)
