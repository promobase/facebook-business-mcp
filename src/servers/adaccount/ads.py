"""Ad operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from src.generated.models import AdAccountCreateAdParams, AdAccountField
from src.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def get_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ads of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)


@wrapped_fn_tool
def create_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountCreateAdParams = {},
) -> AdAccountField:
    """create a new ad in the ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).create_ad(fields=fields, params=params)
