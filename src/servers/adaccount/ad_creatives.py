"""Ad Creative operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from src.generated.models import AdAccountField
from src.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def get_ad_creatives(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad creatives of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).get_ad_creatives(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new ad creative in the ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).create_ad_creative(fields=fields, params=params)
