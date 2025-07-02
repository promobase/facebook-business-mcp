"""
Auto-generated MCP server for Facebook LeadGenDataDraft.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgendatadraft")


# CRUD Operations


@mcp.tool()
async def api_create_leadgendatadraft(
    leadgendatadraft_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenDataDraft(fbid=leadgendatadraft_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_leadgendatadraft(
    leadgendatadraft_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenDataDraft(fbid=leadgendatadraft_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_leadgendatadraft(
    leadgendatadraft_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenDataDraft(fbid=leadgendatadraft_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_leadgendatadraft(
    leadgendatadraft_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LeadGenDataDraft(fbid=leadgendatadraft_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgendatadraft_server = mcp
