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
    """Get ads for an ad set."""
    adset = AdSet(adset_id)
    return adset.get_ads(fields=fields, params=params)


@handle_facebook_errors
def adset_get_ad_creatives(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad creatives for an ad set."""
    adset = AdSet(adset_id)
    return adset.get_ad_creatives(fields=fields, params=params)


@handle_facebook_errors
def adset_create_ad_label(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad label for an ad set."""
    adset = AdSet(adset_id)
    return adset.create_ad_label(fields=fields, params=params)


@handle_facebook_errors
def adset_delete_ad_labels(
    adset_id: str, params: dict[str, Any] = {}, fields: list[str] = []
) -> dict[str, Any]:
    """Delete ad labels from an ad set."""
    adset = AdSet(adset_id)
    return adset.delete_ad_labels(fields=fields, params=params)


@handle_facebook_errors
def adset_get_ad_rules_governed(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get ad rules that govern this ad set."""
    adset = AdSet(adset_id)
    return adset.get_ad_rules_governed(fields=fields, params=params)
