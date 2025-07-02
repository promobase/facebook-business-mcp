"""
Auto-generated MCP server for Facebook EventSourceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventsourcegroup")


# CRUD Operations


@mcp.tool()
async def create_eventsourcegroup(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a EventSourceGroup.

    Args:
        object_id: The ID of the EventSourceGroup
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = EventSourceGroup(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventSourceGroup.

    Args:
        object_id: The ID of the EventSourceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventSourceGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a EventSourceGroup.

    Args:
        object_id: The ID of the EventSourceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = EventSourceGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_shared_account_for_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Shared Account for EventSourceGroup.

    Args:
        object_id: The ID of the EventSourceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_shared_account result
    """
    result = EventSourceGroup(fbid=object_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts_for_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shared Accounts for EventSourceGroup.

    Args:
        object_id: The ID of the EventSourceGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_accounts result
    """
    result = EventSourceGroup(fbid=object_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventsourcegroup_server = mcp
