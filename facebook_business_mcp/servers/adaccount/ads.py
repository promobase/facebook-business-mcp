"""Ad operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.generated.models import AdAccountCreateAdParams, AdAccountField
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def get_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ads of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)
