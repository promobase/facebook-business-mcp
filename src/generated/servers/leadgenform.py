"""
Auto-generated MCP server for Facebook LeadgenForm.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenform import LeadgenForm
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenform")


# CRUD Operations


@mcp.tool()
async def get_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LeadgenForm.

    Args:
        object_id: The ID of the LeadgenForm
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LeadgenForm(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a LeadgenForm.

    Args:
        object_id: The ID of the LeadgenForm
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = LeadgenForm(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_test_lead_for_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Test Lead for LeadgenForm.

    Args:
        object_id: The ID of the LeadgenForm
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_test_lead result
    """
    result = LeadgenForm(fbid=object_id).create_test_lead(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_leads_for_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Leads for LeadgenForm.

    Args:
        object_id: The ID of the LeadgenForm
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_leads result
    """
    result = LeadgenForm(fbid=object_id).get_leads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_test_leads_for_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Test Leads for LeadgenForm.

    Args:
        object_id: The ID of the LeadgenForm
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_test_leads result
    """
    result = LeadgenForm(fbid=object_id).get_test_leads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenform_server = mcp
