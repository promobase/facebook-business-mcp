"""AdCreative CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook ad creatives.
"""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative

from facebook_business_mcp.utils import handle_facebook_errors, use_adaccount_id


class CommonAdCreativeFields:
    """
    A class to hold common sets of fields for Facebook Ad Creatives.
    Fields are grouped by estimated usage frequency.
    """

    high_frequency = [
        AdCreative.Field.id,
        AdCreative.Field.name,
        AdCreative.Field.status,
        AdCreative.Field.body,
        AdCreative.Field.title,
        AdCreative.Field.image_url,
        AdCreative.Field.video_id,
        AdCreative.Field.object_story_spec,
    ]
    medium_frequency = [
        AdCreative.Field.call_to_action_type,
        AdCreative.Field.link_url,
        AdCreative.Field.thumbnail_url,
        AdCreative.Field.asset_feed_spec,
        AdCreative.Field.object_type,
        AdCreative.Field.instagram_permalink_url,
        AdCreative.Field.effective_object_story_id,
    ]
    low_frequency = [
        AdCreative.Field.account_id,
        AdCreative.Field.actor_id,
        AdCreative.Field.adlabels,
        AdCreative.Field.applink_treatment,
        AdCreative.Field.branded_content,
        AdCreative.Field.platform_customizations,
        AdCreative.Field.url_tags,
        AdCreative.Field.product_set_id,
    ]
    basic = list(set(high_frequency + medium_frequency))


@handle_facebook_errors
def adcreative_api_get(
    creative_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Get an ad creative. If no fields are specified, will fallback to use basic fields.

    Args:
        creative_id: The ad creative ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Ad creative data from the API
    """
    creative = AdCreative(creative_id)
    if not fields:
        fields = CommonAdCreativeFields.basic
    return creative.api_get(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_create(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad creative using the Facebook API.

    This is a direct wrapper around AdAccount.create_ad_creative().

    Args:
        account_id: The ad account ID (with or without 'act_' prefix)
        params: Ad creative creation parameters
        fields: Fields to return in the response

    Returns:
        Created ad creative data
    """
    account_id = use_adaccount_id(account_id)
    account = AdAccount(account_id)
    return account.create_ad_creative(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_update(
    creative_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Update an ad creative."""
    creative = AdCreative(creative_id)
    if not fields:
        fields = CommonAdCreativeFields.basic
    return creative.api_update(fields=fields, params=params)


@handle_facebook_errors
def adcreative_api_delete(creative_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete an ad creative."""
    creative = AdCreative(creative_id)
    return creative.api_delete(params=params)
