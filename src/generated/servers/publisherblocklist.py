"""
Auto-generated MCP server for Facebook PublisherBlockList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.publisherblocklist import PublisherBlockList
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-publisherblocklist")


# CRUD Operations


@mcp.tool()
async def create_publisherblocklist(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = PublisherBlockList(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_publisherblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = PublisherBlockList(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_publisherblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PublisherBlockList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_publisherblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = PublisherBlockList(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_append_publisher_url_for_publisherblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Append Publisher Url for PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_append_publisher_url result
    """
    result = PublisherBlockList(fbid=object_id).create_append_publisher_url(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_paged_web_publishers_for_publisherblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Paged Web Publishers for PublisherBlockList.

    Args:
        object_id: The ID of the PublisherBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_paged_web_publishers result
    """
    result = PublisherBlockList(fbid=object_id).get_paged_web_publishers(
        fields=fields,
        params=params,
    )

    return result


# Export the server
publisherblocklist_server = mcp
