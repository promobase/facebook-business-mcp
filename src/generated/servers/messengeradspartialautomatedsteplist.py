"""
Auto-generated MCP server for Facebook MessengerAdsPartialAutomatedStepList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepList,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-messengeradspartialautomatedsteplist")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    messengeradspartialautomatedsteplist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_steps(
    messengeradspartialautomatedsteplist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerAdsPartialAutomatedStepList(
        fbid=messengeradspartialautomatedsteplist_id
    ).get_steps(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengeradspartialautomatedsteplist_server = mcp
