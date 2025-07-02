"""
Auto-generated MCP server for Facebook AdRuleExecutionSpec.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adruleexecutionspec import AdRuleExecutionSpec
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adruleexecutionspec")


# CRUD Operations


@mcp.tool()
async def create_adruleexecutionspec(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleExecutionSpec(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adruleexecutionspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleExecutionSpec(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adruleexecutionspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleExecutionSpec(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adruleexecutionspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleExecutionSpec(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adruleexecutionspec_server = mcp
