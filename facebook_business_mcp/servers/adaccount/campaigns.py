"""Campaign-related operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.generated.models import AdAccountField
from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def get_campaigns(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad campaigns of an ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.get_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def create_campaign(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new campaign in the ad account"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.create_campaign(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaigns(
    adaccount_id: str,
    params: dict[
        str,
        Any,
    ] = {},
) -> bool:
    """delete campaigns on an ad account by conditions.
    param_types = {
            "before_date": "datetime",
            "delete_offset": "unsigned int",
            "delete_strategy": "delete_strategy_enum",
            "object_count": "int",
        }
        enums = {
            "delete_strategy_enum": [
                "DELETE_ANY",
                "DELETE_ARCHIVED_BEFORE",
                "DELETE_OLDEST",
            ],
        }
    """
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.delete_campaigns(params=params)
