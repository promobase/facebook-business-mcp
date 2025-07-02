"""
Auto-generated MCP server for Facebook FundraiserPersonToCharity.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fundraiserpersontocharity import FundraiserPersonToCharity
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-fundraiserpersontocharity")


# CRUD Operations


@mcp.tool()
async def create_fundraiserpersontocharity(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FundraiserPersonToCharity(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FundraiserPersonToCharity(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_fundraiserpersontocharity(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
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
    result = FundraiserPersonToCharity(fbid=object_id).get_external_donations(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fundraiserpersontocharity_server = mcp
