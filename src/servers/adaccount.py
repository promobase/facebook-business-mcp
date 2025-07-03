from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.generated.models import AdAccountField
from src.utils import with_adaccount_id, wrapped_adaccount_tool, wrapped_fn_tool

server_name = "FacebookAdAccount"
instructions = """
AdAccount MCP Server for Facebook Business API.

Provides typed access to all AdAccount operations.
"""

adaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD ----
@wrapped_adaccount_tool
def api_get(adaccount_id: str, fields: list[str] = []) -> AdAccount:
    """get ad account by ID
    Specify fields to retrieve.
    """
    ad_account = AdAccount(adaccount_id)
    return ad_account.api_get(fields=fields)


@wrapped_adaccount_tool
def api_update(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """updates an ad account by ID"""
    ad_account = AdAccount(adaccount_id)
    return ad_account.api_update(fields=fields, params=params)


#  ---- campaigns ----
@wrapped_adaccount_tool
def get_campains(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad campaigns of an ad account"""
    ad_account = AdAccount(adaccount_id)
    return ad_account.get_campaigns(fields=fields, params=params)


@wrapped_adaccount_tool
def create_campaign(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new campaign in the ad account"""
    ad_account = AdAccount(adaccount_id)
    return ad_account.create_campaign(fields=fields, params=params)


@wrapped_adaccount_tool
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
    ad_account = AdAccount(adaccount_id)
    return ad_account.delete_campaigns(params=params)


# ---- ad sets -----
@wrapped_adaccount_tool
def get_ad_sets(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad sets of an ad account"""
    ad_account = AdAccount(adaccount_id)
    return ad_account.get_ad_sets(fields=fields, params=params)


@wrapped_adaccount_tool
def create_ad_set(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new ad set in the ad account"""
    ad_account = AdAccount(adaccount_id)
    return ad_account.create_ad_set(fields=fields, params=params)


# ---- Ads ----
@wrapped_adaccount_tool
def get_ads(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ads of an ad account"""
    return AdAccount(adaccount_id).get_ads(fields=fields, params=params)


@wrapped_adaccount_tool
def create_ad(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new ad in the ad account"""
    return AdAccount(adaccount_id).create_ad(fields=fields, params=params)


# ---- ad creatives ----
@wrapped_adaccount_tool
def get_ad_creatives(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> list[AdAccountField]:
    """get all ad creatives of an ad account"""
    return AdAccount(adaccount_id).get_ad_creatives(fields=fields, params=params)


@wrapped_adaccount_tool
def create_ad_creative(
    adaccount_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> AdAccountField:
    """create a new ad creative in the ad account"""
    return AdAccount(adaccount_id).create_ad_creative(fields=fields, params=params)


# ---- register tools ----
adaccount_server.tool(api_get)
adaccount_server.tool(api_update)
adaccount_server.tool(get_campains)
adaccount_server.tool(create_campaign)
adaccount_server.tool(delete_campaigns)
adaccount_server.tool(get_ad_sets)
adaccount_server.tool(create_ad_set)
