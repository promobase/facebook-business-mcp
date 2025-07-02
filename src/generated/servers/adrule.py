"""
Auto-generated MCP server for Facebook AdRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adrule import AdRule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adrule")


# CRUD Operations


@mcp.tool()
async def create_adrule(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdRule.

    Args:
        object_id: The ID of the AdRule
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdRule(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdRule(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdRule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdRule(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_execute_for_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Execute for AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_execute result
    """
    result = AdRule(fbid=object_id).create_execute(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_preview_for_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Preview for AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_preview result
    """
    result = AdRule(fbid=object_id).create_preview(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_history_for_adrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get History for AdRule.

    Args:
        object_id: The ID of the AdRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_history result
    """
    result = AdRule(fbid=object_id).get_history(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adrule_server = mcp
