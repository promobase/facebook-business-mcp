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
async def create_adsvalueadjustmentrulecollection(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adsvalueadjustmentrulecollection(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adsvalueadjustmentrulecollection(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adsvalueadjustmentrulecollection(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_delete_rule_set_for_adsvalueadjustmentrulecollection(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).create_delete_rule_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rules_for_adsvalueadjustmentrulecollection(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).get_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsvalueadjustmentrulecollection_server = mcp
