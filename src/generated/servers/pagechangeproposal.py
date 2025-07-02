"""
Auto-generated MCP server for Facebook PageChangeProposal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagechangeproposal import PageChangeProposal
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagechangeproposal")


# CRUD Operations


@mcp.tool()
async def api_create_pagechangeproposal(
    pagechangeproposal_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageChangeProposal(fbid=pagechangeproposal_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagechangeproposal(
    pagechangeproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageChangeProposal(fbid=pagechangeproposal_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagechangeproposal(
    pagechangeproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageChangeProposal(fbid=pagechangeproposal_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagechangeproposal(
    pagechangeproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageChangeProposal(fbid=pagechangeproposal_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagechangeproposal_server = mcp
