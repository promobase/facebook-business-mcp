"""Ad Set operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.generated.models import AdAccountField, AdAccountGetAdSetsParams
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def adaccount_get_ad_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: AdAccountGetAdSetsParams = {},
) -> list[AdAccountField]:
    """get all ad sets of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.get_ad_sets(fields=fields, params=params)
