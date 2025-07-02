"""
Auto-generated MCP server for Facebook CustomConversion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.customconversion import CustomConversion
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-customconversion")


# CRUD Operations


@mcp.tool()
async def create_customconversion(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a CustomConversion.

    Args:
        object_id: The ID of the CustomConversion
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = CustomConversion(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_customconversion(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a CustomConversion.

    Args:
        object_id: The ID of the CustomConversion
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = CustomConversion(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_customconversion(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CustomConversion.

    Args:
        object_id: The ID of the CustomConversion
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CustomConversion(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_customconversion(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a CustomConversion.

    Args:
        object_id: The ID of the CustomConversion
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = CustomConversion(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_stats_for_customconversion(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Stats for CustomConversion.

    Args:
        object_id: The ID of the CustomConversion
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stats result
    """
    result = CustomConversion(fbid=object_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
customconversion_server = mcp
