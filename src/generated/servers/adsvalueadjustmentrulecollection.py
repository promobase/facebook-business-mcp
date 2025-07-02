"""
Auto-generated MCP server for Facebook AdsValueAdjustmentRuleCollection.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollection,
)
from facebook_business.api import FacebookAdsApi
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
    """
    Create a AdsValueAdjustmentRuleCollection.

    Args:
        object_id: The ID of the AdsValueAdjustmentRuleCollection
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).api_create(
        parent_id=parent_id,
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
    """
    Get a AdsValueAdjustmentRuleCollection.

    Args:
        object_id: The ID of the AdsValueAdjustmentRuleCollection
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a AdsValueAdjustmentRuleCollection.

    Args:
        object_id: The ID of the AdsValueAdjustmentRuleCollection
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Delete Rule Set for AdsValueAdjustmentRuleCollection.

    Args:
        object_id: The ID of the AdsValueAdjustmentRuleCollection
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_delete_rule_set result
    """
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
    """
    Get Rules for AdsValueAdjustmentRuleCollection.

    Args:
        object_id: The ID of the AdsValueAdjustmentRuleCollection
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_rules result
    """
    result = AdsValueAdjustmentRuleCollection(fbid=object_id).get_rules(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsvalueadjustmentrulecollection_server = mcp
