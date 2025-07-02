"""
Auto-generated MCP server for Facebook MessengerAdsPartialAutomatedStepList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengeradspartialautomatedsteplist import (
    MessengerAdsPartialAutomatedStepList,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-messengeradspartialautomatedsteplist")


# CRUD Operations


@mcp.tool()
async def get_messengeradspartialautomatedsteplist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MessengerAdsPartialAutomatedStepList.

    Args:
        object_id: The ID of the MessengerAdsPartialAutomatedStepList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).api_get(
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
    """
    Get Steps for MessengerAdsPartialAutomatedStepList.

    Args:
        object_id: The ID of the MessengerAdsPartialAutomatedStepList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_steps result
    """
    result = MessengerAdsPartialAutomatedStepList(fbid=object_id).get_steps(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengeradspartialautomatedsteplist_server = mcp
