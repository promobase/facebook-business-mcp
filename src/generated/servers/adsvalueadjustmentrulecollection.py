"""AdsValueAdjustmentRuleCollection MCP Server."""

from typing import Any

from facebook_business.adobjects.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollection,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsValueAdjustmentRuleCollection"
instructions = """
AdsValueAdjustmentRuleCollection MCP Server for Facebook Business API.

Provides typed access to all AdsValueAdjustmentRuleCollection operations.
"""

adsvalueadjustmentrulecollection_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def get_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsValueAdjustmentRuleCollection(adsvalueadjustmentrulecollection_id)
    return obj.api_get(fields=fields)


@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def update_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdsValueAdjustmentRuleCollection(adsvalueadjustmentrulecollection_id).api_update(
        fields=fields, params=params
    )


# ---- Edge Methods (2) ----
@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def create_delete_rule_set(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsValueAdjustmentRuleCollection(
        adsvalueadjustmentrulecollection_id
    ).create_delete_rule_set(fields=fields, params=params)


@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def get_rules(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsValueAdjustmentRuleCollection(adsvalueadjustmentrulecollection_id).get_rules(
        fields=fields, params=params
    )
