"""CRUD operations for AdAccount."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount

from facebook_business_mcp.utils import use_adaccount_id, wrapped_fn_tool


@wrapped_fn_tool
def adaccount_api_get(adaccount_id: str, fields: list[str] = []) -> AdAccount:
    """get ad account by ID
    Specify fields to retrieve.
    """
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.api_get(fields=fields)


@wrapped_fn_tool
def adaccount_api_update(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """updates an ad account by ID"""
    adaccount_id = use_adaccount_id(adaccount_id)
    ad_account = AdAccount(adaccount_id)
    return ad_account.api_update(fields=fields, params=params)
