"""
Auto-generated MCP server for Facebook OffsiteSignalContainerBusinessObject.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offsitesignalcontainerbusinessobject import (
    OffsiteSignalContainerBusinessObject,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offsitesignalcontainerbusinessobject")


# CRUD Operations


@mcp.tool()
async def get_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OffsiteSignalContainerBusinessObject.

    Args:
        object_id: The ID of the OffsiteSignalContainerBusinessObject
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_linked_application_for_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Linked Application for OffsiteSignalContainerBusinessObject.

    Args:
        object_id: The ID of the OffsiteSignalContainerBusinessObject
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_linked_application result
    """
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).get_linked_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_linked_page_for_offsitesignalcontainerbusinessobject(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Linked Page for OffsiteSignalContainerBusinessObject.

    Args:
        object_id: The ID of the OffsiteSignalContainerBusinessObject
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_linked_page result
    """
    result = OffsiteSignalContainerBusinessObject(fbid=object_id).get_linked_page(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offsitesignalcontainerbusinessobject_server = mcp
