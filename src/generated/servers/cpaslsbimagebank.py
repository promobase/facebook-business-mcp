"""
Auto-generated MCP server for Facebook CPASLsbImageBank.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpaslsbimagebank import CPASLsbImageBank
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpaslsbimagebank")


# CRUD Operations


@mcp.tool()
async def create_cpaslsbimagebank(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a CPASLsbImageBank.

    Args:
        object_id: The ID of the CPASLsbImageBank
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = CPASLsbImageBank(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpaslsbimagebank(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASLsbImageBank.

    Args:
        object_id: The ID of the CPASLsbImageBank
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASLsbImageBank(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_cpaslsbimagebank(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a CPASLsbImageBank.

    Args:
        object_id: The ID of the CPASLsbImageBank
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = CPASLsbImageBank(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_backup_images_for_cpaslsbimagebank(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Backup Images for CPASLsbImageBank.

    Args:
        object_id: The ID of the CPASLsbImageBank
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_backup_images result
    """
    result = CPASLsbImageBank(fbid=object_id).get_backup_images(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpaslsbimagebank_server = mcp
