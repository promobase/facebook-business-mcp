"""
Auto-generated MCP server for Facebook TargetingSentenceLine.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-targetingsentenceline")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    targetingsentenceline_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
targetingsentenceline_server = mcp
