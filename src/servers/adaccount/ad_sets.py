"""Ad Set operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from src.generated.models import AdAccountField
from src.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def get_ad_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad sets of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.get_ad_sets(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new ad set in the ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.create_ad_set(fields=fields, params=params)
