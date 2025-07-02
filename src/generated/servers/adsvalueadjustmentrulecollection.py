"""
Auto-generated MCP server for Facebook AdsValueAdjustmentRuleCollection.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollection,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsvalueadjustmentrulecollection")


# CRUD Operations


@mcp.tool()
async def api_create_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=adsvalueadjustmentrulecollection_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=adsvalueadjustmentrulecollection_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=adsvalueadjustmentrulecollection_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=adsvalueadjustmentrulecollection_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_delete_rule_set(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(
        fbid=adsvalueadjustmentrulecollection_id
    ).create_delete_rule_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rules(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=adsvalueadjustmentrulecollection_id).get_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsvalueadjustmentrulecollection_server = mcp
