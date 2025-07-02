"""
Auto-generated MCP server for Facebook ExtendedCredit.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.extendedcredit import ExtendedCredit
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-extendedcredit")


# CRUD Operations


@mcp.tool()
async def get_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ExtendedCredit(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_extended_credit_invoice_group_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Extended Credit Invoice Group for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_extended_credit_invoice_group result
    """
    result = ExtendedCredit(fbid=object_id).create_extended_credit_invoice_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_owning_credit_allocation_config_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Owning Credit Allocation Config for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_owning_credit_allocation_config result
    """
    result = ExtendedCredit(fbid=object_id).create_owning_credit_allocation_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_attach_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Whats App Credit Attach for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_whats_app_credit_attach result
    """
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_sharing_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Whats App Credit Sharing for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_whats_app_credit_sharing result
    """
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_sharing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_whats_app_credit_sharing_and_attach_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Whats App Credit Sharing And Attach for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_whats_app_credit_sharing_and_attach result
    """
    result = ExtendedCredit(fbid=object_id).create_whats_app_credit_sharing_and_attach(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_extended_credit_invoice_groups_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Extended Credit Invoice Groups for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_extended_credit_invoice_groups result
    """
    result = ExtendedCredit(fbid=object_id).get_extended_credit_invoice_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_owning_credit_allocation_configs_for_extendedcredit(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Owning Credit Allocation Configs for ExtendedCredit.

    Args:
        object_id: The ID of the ExtendedCredit
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_owning_credit_allocation_configs result
    """
    result = ExtendedCredit(fbid=object_id).get_owning_credit_allocation_configs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
extendedcredit_server = mcp
