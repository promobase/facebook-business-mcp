"""
Auto-generated MCP server for Facebook LeadGenLegalContent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenlegalcontent import LeadGenLegalContent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenlegalcontent")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    leadgenlegalcontent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenLegalContent(fbid=leadgenlegalcontent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    leadgenlegalcontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenLegalContent(fbid=leadgenlegalcontent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    leadgenlegalcontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenLegalContent(fbid=leadgenlegalcontent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    leadgenlegalcontent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenLegalContent(fbid=leadgenlegalcontent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenlegalcontent_server = mcp
