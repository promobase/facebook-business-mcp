"""
Auto-generated MCP server for Facebook LeadGenLegalContentCheckbox.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenlegalcontentcheckbox import LeadGenLegalContentCheckbox
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenlegalcontentcheckbox")


# CRUD Operations


@mcp.tool()
async def api_create_leadgenlegalcontentcheckbox(
    leadgenlegalcontentcheckbox_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenLegalContentCheckbox(fbid=leadgenlegalcontentcheckbox_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_leadgenlegalcontentcheckbox(
    leadgenlegalcontentcheckbox_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenLegalContentCheckbox(fbid=leadgenlegalcontentcheckbox_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_leadgenlegalcontentcheckbox(
    leadgenlegalcontentcheckbox_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenLegalContentCheckbox(fbid=leadgenlegalcontentcheckbox_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_leadgenlegalcontentcheckbox(
    leadgenlegalcontentcheckbox_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenLegalContentCheckbox(fbid=leadgenlegalcontentcheckbox_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenlegalcontentcheckbox_server = mcp
