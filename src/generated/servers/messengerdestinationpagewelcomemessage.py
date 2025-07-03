"""
Auto-generated MCP server for Facebook MessengerDestinationPageWelcomeMessage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messengerdestinationpagewelcomemessage import (
    MessengerDestinationPageWelcomeMessage,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-messengerdestinationpagewelcomemessage")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    messengerdestinationpagewelcomemessage_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerDestinationPageWelcomeMessage(
        fbid=messengerdestinationpagewelcomemessage_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    messengerdestinationpagewelcomemessage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerDestinationPageWelcomeMessage(
        fbid=messengerdestinationpagewelcomemessage_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    messengerdestinationpagewelcomemessage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerDestinationPageWelcomeMessage(
        fbid=messengerdestinationpagewelcomemessage_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    messengerdestinationpagewelcomemessage_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessengerDestinationPageWelcomeMessage(
        fbid=messengerdestinationpagewelcomemessage_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messengerdestinationpagewelcomemessage_server = mcp
