"""
Auto-generated MCP server for Facebook LeadGenThankYouPage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.leadgenthankyoupage import LeadGenThankYouPage
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-leadgenthankyoupage")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    leadgenthankyoupage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenThankYouPage(fbid=leadgenthankyoupage_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    leadgenthankyoupage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenThankYouPage(fbid=leadgenthankyoupage_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    leadgenthankyoupage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenThankYouPage(fbid=leadgenthankyoupage_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    leadgenthankyoupage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LeadGenThankYouPage(fbid=leadgenthankyoupage_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
leadgenthankyoupage_server = mcp
