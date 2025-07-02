"""
Auto-generated MCP server for Facebook TargetingSentenceLine.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-targetingsentenceline")


# CRUD Operations


@mcp.tool()
async def api_create_targetingsentenceline(
    targetingsentenceline_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_targetingsentenceline(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_targetingsentenceline(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_targetingsentenceline(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=targetingsentenceline_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
targetingsentenceline_server = mcp
