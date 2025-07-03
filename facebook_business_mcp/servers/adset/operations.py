"""AdSet additional operations.

This module provides thin wrappers around AdSet SDK methods for various operations.
"""

from typing import Any

from facebook_business.adobjects.adset import AdSet

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def adset_get_activities(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get activities for an ad set.

    This is a direct wrapper around AdSet.get_activities().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of activities
    """
    adset = AdSet(adset_id)
    return adset.get_activities(fields=fields, params=params)


@handle_facebook_errors
def adset_get_copies(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get copies of an ad set.

    This is a direct wrapper around AdSet.get_copies().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of ad set copies
    """
    adset = AdSet(adset_id)
    return adset.get_copies(fields=fields, params=params)


@handle_facebook_errors
def adset_create_copy(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create a copy of an ad set.

    This is a direct wrapper around AdSet.create_copy().

    Args:
        adset_id: The ad set ID to copy
        params: Copy parameters (e.g., deep_copy, rename_options)
        fields: Fields to return

    Returns:
        Created ad set copy data
    """
    adset = AdSet(adset_id)
    return adset.create_copy(fields=fields, params=params)


@handle_facebook_errors
def adset_create_budget_schedule(
    adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create a budget schedule for an ad set.

    This is a direct wrapper around AdSet.create_budget_schedule().

    Args:
        adset_id: The ad set ID
        params: Budget schedule parameters
        fields: Fields to return

    Returns:
        Created budget schedule data
    """
    adset = AdSet(adset_id)
    return adset.create_budget_schedule(fields=fields, params=params)


@handle_facebook_errors
def adset_get_async_ad_requests(
    adset_id: str, fields: list[str] = [], params: dict[str, Any] = {}
) -> list[dict[str, Any]]:
    """Get async ad requests for an ad set.

    This is a direct wrapper around AdSet.get_async_ad_requests().

    Args:
        adset_id: The ad set ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        List of async ad requests
    """
    adset = AdSet(adset_id)
    return adset.get_async_ad_requests(fields=fields, params=params)
