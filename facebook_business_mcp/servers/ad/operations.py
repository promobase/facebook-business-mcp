"""Ad operations.

This module provides additional operations for Facebook ads beyond basic CRUD.
"""

from typing import Any

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.utils import handle_facebook_errors, use_adaccount_id, wrapped_fn_tool


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
) -> Any:
    """get all ads of an ad account. If no fields, we will use basic fields for most frequent fields access."""
    adaccount_id = use_adaccount_id(adaccount_id)
    if not fields:
        fields = CommonAdFields.basic
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)


@handle_facebook_errors
def ad_get_adcreatives(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get ad creatives for an ad.

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve for the ad creatives
        params: Additional parameters

    Returns:
        List of ad creatives
    """
    ad = Ad(ad_id)
    return ad.get_ad_creatives(fields=fields, params=params)


@handle_facebook_errors
def ad_get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    time_range: dict[str, str] | None = None,
    breakdowns: list[str] = [],
) -> dict[str, Any]:
    """Get insights (performance metrics) for an ad.

    Args:
        ad_id: The ad ID
        fields: Metrics to retrieve (e.g., ["impressions", "clicks", "spend"])
        params: Additional parameters
        time_range: Date range (e.g., {"since": "2024-01-01", "until": "2024-01-31"})
        breakdowns: Dimensions to break down metrics by (e.g., ["age", "gender"])

    Returns:
        Performance metrics for the ad
    """
    ad = Ad(ad_id)

    # Add commonly requested fields if none specified
    if not fields:
        fields = [
            "impressions",
            "clicks",
            "spend",
            "reach",
            "cpm",
            "cpc",
            "ctr",
        ]

    # Add time range and breakdowns to params if provided
    if time_range:
        params["time_range"] = time_range
    if breakdowns:
        params["breakdowns"] = breakdowns

    return ad.get_insights(fields=fields, params=params)


@handle_facebook_errors
def ad_get_targetingsentencelines(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get human-readable targeting description for an ad.

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Targeting sentence lines
    """
    ad = Ad(ad_id)
    return ad.get_targeting_sentence_lines(fields=fields, params=params)


@handle_facebook_errors
def ad_get_previews(
    ad_id: str,
    ad_format: str = "DESKTOP_FEED_STANDARD",
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """Get ad previews for different placements.

    Args:
        ad_id: The ad ID
        ad_format: Preview format (e.g., "DESKTOP_FEED_STANDARD", "MOBILE_FEED_STANDARD", "INSTAGRAM_STANDARD", "INSTAGRAM_STORY")
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Ad preview data
    """
    ad = Ad(ad_id)
    params["ad_format"] = ad_format
    return ad.get_previews(fields=fields, params=params)


@handle_facebook_errors
def ad_get_leads(ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}) -> dict[str, Any]:
    """Get leads from a lead generation ad.

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve for each lead
        params: Additional parameters

    Returns:
        List of leads
    """
    ad = Ad(ad_id)
    return ad.get_leads(fields=fields, params=params)


@handle_facebook_errors
def ad_pause(ad_id: str) -> dict[str, Any]:
    """Pause an active ad.

    Args:
        ad_id: The ad ID

    Returns:
        Updated ad data
    """
    ad = Ad(ad_id)
    return ad.api_update(params={"status": "PAUSED"})


@handle_facebook_errors
def ad_resume(ad_id: str) -> dict[str, Any]:
    """Resume a paused ad.

    Args:
        ad_id: The ad ID

    Returns:
        Updated ad data
    """
    ad = Ad(ad_id)
    return ad.api_update(params={"status": "ACTIVE"})


@handle_facebook_errors
def ad_archive(ad_id: str) -> dict[str, Any]:
    """Archive an ad (can be unarchived later).

    Args:
        ad_id: The ad ID

    Returns:
        Updated ad data
    """
    ad = Ad(ad_id)
    return ad.api_update(params={"status": "ARCHIVED"})


@handle_facebook_errors
def ad_add_labels(ad_id: str, adlabel_ids: list[str]) -> dict[str, Any]:
    """Add labels to an ad for organization and filtering.

    Args:
        ad_id: The ad ID
        adlabel_ids: List of ad label IDs to add

    Returns:
        Success response
    """
    ad = Ad(ad_id)
    return ad.add_labels(adlabel_ids=adlabel_ids)


@handle_facebook_errors
def ad_create_copy(
    ad_id: str,
    adset_id: str,
    rename_options: dict[str, Any] | None = None,
    status_option: str = "PAUSED",
) -> dict[str, Any]:
    """Create a copy of an existing ad.

    Args:
        ad_id: The ad ID to copy
        adset_id: The target ad set ID
        rename_options: Options for renaming (e.g., {"rename_suffix": " - Copy"})
        status_option: Initial status for the copy ("PAUSED" or "INHERITED")

    Returns:
        Created ad copy data
    """
    ad = Ad(ad_id)
    params = {
        "adset_id": adset_id,
        "status_option": status_option,
    }
    if rename_options:
        params["rename_options"] = rename_options

    return ad.create_copy(params=params)


@handle_facebook_errors
def ad_get_copies(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    effective_status: list[str] | None = None,
) -> dict[str, Any]:
    """Get copies of an ad.

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve for each copy
        params: Additional parameters
        effective_status: Filter by status (e.g., ["ACTIVE", "PAUSED"])

    Returns:
        List of ad copies
    """
    ad = Ad(ad_id)

    if not fields:
        fields = CommonAdFields.basic

    if effective_status:
        params["effective_status"] = effective_status

    return ad.get_copies(fields=fields, params=params)
