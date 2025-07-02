"""
Auto-generated MCP server for Facebook ChinaBusinessOnboardingVettingRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.chinabusinessonboardingvettingrequest import (
    ChinaBusinessOnboardingVettingRequest,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-chinabusinessonboardingvettingrequest")


# CRUD Operations


@mcp.tool()
async def api_create_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChinaBusinessOnboardingVettingRequest(
        fbid=chinabusinessonboardingvettingrequest_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChinaBusinessOnboardingVettingRequest(
        fbid=chinabusinessonboardingvettingrequest_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChinaBusinessOnboardingVettingRequest(
        fbid=chinabusinessonboardingvettingrequest_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChinaBusinessOnboardingVettingRequest(
        fbid=chinabusinessonboardingvettingrequest_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
chinabusinessonboardingvettingrequest_server = mcp
