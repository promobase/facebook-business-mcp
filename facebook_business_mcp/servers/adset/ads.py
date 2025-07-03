"""AdSet Ads operations.

This module provides thin wrappers around AdSet SDK methods for ads.
"""

from typing import Any

from facebook_business.adobjects.adset import AdSet

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def adset_get_ads(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ads for an ad set.

    This is a direct wrapper around AdSet.get_ads().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters (e.g., filtering, pagination)

    Returns:
        List of ads
    """
    adset = AdSet(adset_id)
    return adset.get_ads(fields=fields, params=params)


@handle_facebook_errors
def adset_get_ad_creatives(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad creatives for an ad set.

    This is a direct wrapper around AdSet.get_ad_creatives().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad creatives
    """
    adset = AdSet(adset_id)
    return adset.get_ad_creatives(fields=fields, params=params)


@handle_facebook_errors
def adset_create_ad_label(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad label for an ad set.

    This is a direct wrapper around AdSet.create_ad_label().

    Args:
        adset_id: The ad set ID
        params: Ad label parameters
        fields: Fields to return

    Returns:
        Created ad label data
    """
    adset = AdSet(adset_id)
    return adset.create_ad_label(fields=fields, params=params)


@handle_facebook_errors
def adset_delete_ad_labels(
    adset_id: str, params: dict[str, Any] = {}, fields: list[str] = []
) -> dict[str, Any]:
    """Delete ad labels from an ad set.

    This is a direct wrapper around AdSet.delete_ad_labels().

    Args:
        adset_id: The ad set ID
        params: Parameters for deletion
        fields: Fields to return

    Returns:
        Deletion result
    """
    adset = AdSet(adset_id)
    return adset.delete_ad_labels(fields=fields, params=params)


@handle_facebook_errors
def adset_get_ad_rules_governed(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad rules that govern this ad set.

    This is a direct wrapper around AdSet.get_ad_rules_governed().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad rules
    """
    adset = AdSet(adset_id)
    return adset.get_ad_rules_governed(fields=fields, params=params)
