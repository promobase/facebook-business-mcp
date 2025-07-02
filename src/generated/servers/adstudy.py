"""
Auto-generated MCP server for Facebook AdStudy.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudy import AdStudy
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudy")


# CRUD Operations


@mcp.tool()
async def create_adstudy(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdStudy.

    Args:
        object_id: The ID of the AdStudy
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdStudy(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdStudy(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdStudy(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdStudy(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_check_point_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Check Point for AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_check_point result
    """
    result = AdStudy(fbid=object_id).create_check_point(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_instance_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Instance for AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_instance result
    """
    result = AdStudy(fbid=object_id).create_instance(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cells_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Cells for AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_cells result
    """
    result = AdStudy(fbid=object_id).get_cells(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instances_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Instances for AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instances result
    """
    result = AdStudy(fbid=object_id).get_instances(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_objectives_for_adstudy(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Objectives for AdStudy.

    Args:
        object_id: The ID of the AdStudy
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_objectives result
    """
    result = AdStudy(fbid=object_id).get_objectives(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudy_server = mcp
