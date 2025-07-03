"""Ad Creative operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.generated.models import AdAccountCreateAdCreativeParams, AdAccountField
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def adaccount_get_ad_creatives(
    adaccount_id: str,
    fields: list[str] = [],
) -> list[AdAccountField]:
    """get all ad creatives of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).get_ad_creatives(fields=fields)
