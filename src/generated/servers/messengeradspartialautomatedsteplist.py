"""
Auto-generated MCP server for Facebook MessengerAdsPartialAutomatedStepList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepList,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-messengeradspartialautomatedsteplist")


# CRUD Operations


@mcp.tool()
async def create_messengeradspartialautomatedsteplist(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_messengeradspartialautomatedsteplist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messengeradspartialautomatedsteplist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_messengeradspartialautomatedsteplist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_steps_for_messengeradspartialautomatedsteplist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).get_steps(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengeradspartialautomatedsteplist_server = mcp
