"""
Auto-generated MCP server for Facebook AdProposal.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adproposal import AdProposal
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adproposal")


# CRUD Operations


@mcp.tool()
async def api_create_adproposal(
    adproposal_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdProposal(fbid=adproposal_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adproposal(
    adproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdProposal(fbid=adproposal_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adproposal(
    adproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdProposal(fbid=adproposal_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adproposal(
    adproposal_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdProposal(fbid=adproposal_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adproposal_server = mcp
