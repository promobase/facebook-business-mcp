"""
Auto-generated MCP server for Facebook LeadgenForm.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenform import LeadgenForm
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenform")


# CRUD Operations


@mcp.tool()
async def create_leadgenform(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_leadgenform(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
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
    result = LeadgenForm(fbid=object_id).get_test_leads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenform_server = mcp
