"""
Auto-generated MCP server for Facebook FundraiserPersonToCharity.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fundraiserpersontocharity import FundraiserPersonToCharity
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-fundraiserpersontocharity")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    fundraiserpersontocharity_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_end_fundraiser(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).create_end_fundraiser(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_external_donation(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).create_external_donation(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_donations(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).get_donations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_external_donations(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = FundraiserPersonToCharity(fbid=fundraiserpersontocharity_id).get_external_donations(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fundraiserpersontocharity_server = mcp
