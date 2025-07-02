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
async def api_create_messengeradspartialautomatedsteplist(
    messengeradspartialautomatedsteplist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_messengeradspartialautomatedsteplist(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_messengeradspartialautomatedsteplist(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_messengeradspartialautomatedsteplist(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_steps(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).get_steps(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengeradspartialautomatedsteplist_server = mcp
