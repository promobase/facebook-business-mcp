"""Ad operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.generated.models import AdAccountCreateAdParams, AdAccountField
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


class CommonAdFields:
    """
    A class to hold common sets of fields for Facebook Ads.
    Fields are grouped by estimated usage frequency.
    """

    high_frequency = [
        Ad.Field.id,
        Ad.Field.name,
        Ad.Field.status,
        Ad.Field.effective_status,
        Ad.Field.adset_id,
        Ad.Field.campaign_id,
        Ad.Field.creative,
    ]
    medium_frequency = [
        Ad.Field.created_time,
        Ad.Field.updated_time,
        Ad.Field.ad_review_feedback,
        Ad.Field.issues_info,
        Ad.Field.adlabels,
        Ad.Field.targeting,
        Ad.Field.bid_amount,
        Ad.Field.preview_shareable_link,
    ]
    low_frequency = [
        Ad.Field.account_id,
        Ad.Field.ad_schedule_start_time,
        Ad.Field.ad_schedule_end_time,
        Ad.Field.bid_info,
        Ad.Field.bid_type,
        Ad.Field.configured_status,
        Ad.Field.conversion_domain,
        Ad.Field.recommendations,
        Ad.Field.source_ad_id,
        Ad.Field.tracking_specs,
        Ad.Field.last_updated_by_app_id,
    ]
    basic = list(set(high_frequency + medium_frequency))


@wrapped_fn_tool
def adaccount_get_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ads of an ad account. If no fields, we will use basic fields for most frequent fields access."""
    adaccount_id = use_adaccount_id(adaccount_id)
    if not fields:
        fields = CommonAdFields.basic
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)
