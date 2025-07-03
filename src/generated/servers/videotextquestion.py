"""
Auto-generated MCP server for Facebook VideoTextQuestion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videotextquestion import VideoTextQuestion
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-videotextquestion")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    videotextquestion_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoTextQuestion(fbid=videotextquestion_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    videotextquestion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoTextQuestion(fbid=videotextquestion_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    videotextquestion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoTextQuestion(fbid=videotextquestion_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    videotextquestion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoTextQuestion(fbid=videotextquestion_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videotextquestion_server = mcp
