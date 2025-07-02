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
async def api_create_leadgenform(
    leadgenform_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_leadgenform(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_leadgenform(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_leadgenform(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_test_lead(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).create_test_lead(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_leads(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).get_leads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_test_leads(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadgenForm(fbid=leadgenform_id).get_test_leads(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenform_server = mcp
