"""
Auto-generated MCP server for Facebook FundraiserPersonToCharity.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fundraiserpersontocharity import FundraiserPersonToCharity
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-fundraiserpersontocharity")


# CRUD Operations


@mcp.tool()
async def get_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FundraiserPersonToCharity(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = FundraiserPersonToCharity(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_end_fundraiser_for_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create End Fundraiser for FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_end_fundraiser result
    """
    result = FundraiserPersonToCharity(fbid=object_id).create_end_fundraiser(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_external_donation_for_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create External Donation for FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_external_donation result
    """
    result = FundraiserPersonToCharity(fbid=object_id).create_external_donation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_donations_for_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Donations for FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_donations result
    """
    result = FundraiserPersonToCharity(fbid=object_id).get_donations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_external_donations_for_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get External Donations for FundraiserPersonToCharity.

    Args:
        object_id: The ID of the FundraiserPersonToCharity
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_external_donations result
    """
    result = FundraiserPersonToCharity(fbid=object_id).get_external_donations(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fundraiserpersontocharity_server = mcp
