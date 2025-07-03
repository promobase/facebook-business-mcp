"""Ad CRUD operations.

This module provides basic Create, Read, Update, and Delete operations for Facebook ads.
"""

from typing import Any

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign

from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def ad_api_get(ad_id: str, fields: list[str] = [], params: dict[str, Any] = {}) -> dict[str, Any]:
    """Get an ad using the Facebook API.

    This is a direct wrapper around Ad.api_get().

    Args:
        ad_id: The ad ID
        fields: Fields to retrieve
        params: Additional parameters

    Returns:
        Ad data from the API
    """

    ad = Ad(ad_id)
    return ad.api_get(fields=fields, params=params)


@handle_facebook_errors
def ad_api_create(adset_id: str, params: dict[str, Any], fields: list[str] = []) -> dict[str, Any]:
    """Create an ad using the Facebook API from an AdSet.

    This is a direct wrapper around AdSet.create_ad().

    Args:
        adset_id: The ad set ID
        params: Ad creation parameters
        fields: Fields to return in the response

    Returns:
        Created ad data
    """
    adset = AdSet(adset_id)
    return adset.create_ad(fields=fields, params=params)


@handle_facebook_errors
def ad_api_create_from_adaccount(
    account_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad directly from an AdAccount.

    This is a direct wrapper around AdAccount.create_ad().
    Note: The params must include 'adset_id' to specify which ad set the ad belongs to.

    Args:
        account_id: The ad account ID (with or without 'act_' prefix)
        params: Ad creation parameters (must include 'adset_id')
        fields: Fields to return in the response

    Returns:
        Created ad data
    """
    # Ensure account_id has the correct prefix
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    
    account = AdAccount(account_id)
    return account.create_ad(fields=fields, params=params)


@handle_facebook_errors
def ad_api_create_from_campaign(
    campaign_id: str, adset_id: str, params: dict[str, Any], fields: list[str] = []
) -> dict[str, Any]:
    """Create an ad within a campaign by specifying the ad set.

    Since Campaign doesn't have a direct create_ad method, this validates
    that the ad set belongs to the campaign before creating the ad.

    Args:
        campaign_id: The campaign ID (for validation)
        adset_id: The ad set ID where the ad will be created
        params: Ad creation parameters
        fields: Fields to return in the response

    Returns:
        Created ad data
    """
    # Validate that the ad set belongs to the campaign
    adset = AdSet(adset_id)
    adset_data = adset.api_get(fields=["campaign_id"])
    
    if adset_data.get("campaign_id") != campaign_id:
        raise ValueError(
            f"Ad set {adset_id} does not belong to campaign {campaign_id}"
        )
    
    # Create the ad through the ad set
    return adset.create_ad(fields=fields, params=params)


@handle_facebook_errors
def ad_api_update(ad_id: str, params: dict[str, Any], fields: list[str] = []) -> dict[str, Any]:
    """Update an ad using the Facebook API.

    This is a direct wrapper around Ad.api_update().

    Args:
        ad_id: The ad ID
        params: Update parameters
        fields: Fields to return in the response

    Returns:
        Updated ad data
    """

    ad = Ad(ad_id)
    return ad.api_update(fields=fields, params=params)


@handle_facebook_errors
def ad_api_delete(ad_id: str, params: dict[str, Any] = {}) -> dict[str, Any]:
    """Delete an ad using the Facebook API.

    This is a direct wrapper around Ad.api_delete().

    Args:
        ad_id: The ad ID
        params: Additional parameters

    Returns:
        Deletion result
    """
    ad = Ad(ad_id)
    return ad.api_delete(params=params)
