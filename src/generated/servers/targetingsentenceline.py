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
async def create_targetingsentenceline(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_targetingsentenceline(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targetingsentenceline(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_targetingsentenceline(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = TargetingSentenceLine(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
targetingsentenceline_server = mcp
