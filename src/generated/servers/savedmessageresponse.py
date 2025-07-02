"""
Auto-generated MCP server for Facebook SavedMessageResponse.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-savedmessageresponse")


# CRUD Operations


@mcp.tool()
async def api_create_savedmessageresponse(
    savedmessageresponse_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SavedMessageResponse(fbid=savedmessageresponse_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_savedmessageresponse(
    savedmessageresponse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SavedMessageResponse(fbid=savedmessageresponse_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_savedmessageresponse(
    savedmessageresponse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SavedMessageResponse(fbid=savedmessageresponse_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_savedmessageresponse(
    savedmessageresponse_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SavedMessageResponse(fbid=savedmessageresponse_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
savedmessageresponse_server = mcp
