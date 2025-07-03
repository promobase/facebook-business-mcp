"""Consolidated Insights operations for all Facebook Business API levels.

This module provides insights operations for AdAccount, Campaign, AdSet, and Ad objects.
"""

from enum import Enum
from typing import Any

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


class InsightsLevel(str, Enum):
    """Supported levels for insights operations."""

    ACCOUNT = "account"
    CAMPAIGN = "campaign"
    ADSET = "adset"
    AD = "ad"


def _get_object_by_level(level: str, object_id: str):
    """Get the appropriate Facebook object based on level."""
    if level == InsightsLevel.ACCOUNT:
        # Ensure account_id has the correct prefix
        if not object_id.startswith("act_"):
            object_id = f"act_{object_id}"
        return AdAccount(object_id)
    elif level == InsightsLevel.CAMPAIGN:
        return Campaign(object_id)
    elif level == InsightsLevel.ADSET:
        return AdSet(object_id)
    elif level == InsightsLevel.AD:
        return Ad(object_id)
    else:
        raise ValueError(
            f"Invalid level: {level}. Must be one of: {[e.value for e in InsightsLevel]}"
        )


@handle_facebook_errors
def get_insights(
    level: str, object_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for any Facebook Business object.

    This is a unified wrapper around get_insights() for all object types.

    Args:
        level: The object level (account, campaign, adset, ad)
        object_id: The object ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., date_preset, breakdowns)

    Returns:
        Insights data from the API
    """
    obj = _get_object_by_level(level, object_id)
    return obj.get_insights(fields=fields, params=params)


@handle_facebook_errors
def get_insights_async(
    level: str, object_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for any Facebook Business object.

    This is a unified wrapper around get_insights_async() for all object types.

    Args:
        level: The object level (account, campaign, adset, ad)
        object_id: The object ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    obj = _get_object_by_level(level, object_id)
    return obj.get_insights_async(fields=fields, params=params)


# Convenience functions for each level
@handle_facebook_errors
def account_get_insights(
    account_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad account.

    This is a direct wrapper around AdAccount.get_insights().

    Args:
        account_id: The ad account ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.ACCOUNT, account_id, fields, params)


@handle_facebook_errors
def account_get_insights_async(
    account_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad account.

    This is a direct wrapper around AdAccount.get_insights_async().

    Args:
        account_id: The ad account ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.ACCOUNT, account_id, fields, params)


@handle_facebook_errors
def campaign_get_insights(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for a campaign.

    This is a direct wrapper around Campaign.get_insights().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.CAMPAIGN, campaign_id, fields, params)


@handle_facebook_errors
def campaign_get_insights_async(
    campaign_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for a campaign.

    This is a direct wrapper around Campaign.get_insights_async().

    Args:
        campaign_id: The campaign ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.CAMPAIGN, campaign_id, fields, params)


@handle_facebook_errors
def adset_get_insights(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad set.

    This is a direct wrapper around AdSet.get_insights().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.ADSET, adset_id, fields, params)


@handle_facebook_errors
def adset_get_insights_async(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad set.

    This is a direct wrapper around AdSet.get_insights_async().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.ADSET, adset_id, fields, params)


@handle_facebook_errors
def ad_get_insights(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get insights for an ad.

    This is a direct wrapper around Ad.get_insights().

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Insights data
    """
    return get_insights(InsightsLevel.AD, ad_id, fields, params)


@handle_facebook_errors
def ad_get_insights_async(
    ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> dict[str, Any]:
    """Start an async insights job for an ad.

    This is a direct wrapper around Ad.get_insights_async().

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Async job details
    """
    return get_insights_async(InsightsLevel.AD, ad_id, fields, params)
