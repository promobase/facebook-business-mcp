"""Campaign-related operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.generated.models import AdAccountField
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


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
    params: dict[
        str,
        Any,
    ] = {},
) -> bool:
    """delete campaigns on an ad account by conditions.
    param_types = {
            "before_date": "datetime",
            "delete_offset": "unsigned int",
            "delete_strategy": "delete_strategy_enum",
            "object_count": "int",
        }
        enums = {
            "delete_strategy_enum": [
                "DELETE_ANY",
                "DELETE_ARCHIVED_BEFORE",
                "DELETE_OLDEST",
            ],
        }
    """
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.delete_campaigns(params=params)
