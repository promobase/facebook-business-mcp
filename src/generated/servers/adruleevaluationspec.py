"""
Auto-generated MCP server for Facebook AdRuleEvaluationSpec.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adruleevaluationspec import AdRuleEvaluationSpec
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adruleevaluationspec")


# CRUD Operations


@mcp.tool()
async def create_adruleevaluationspec(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleEvaluationSpec(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adruleevaluationspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleEvaluationSpec(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adruleevaluationspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleEvaluationSpec(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adruleevaluationspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdRuleEvaluationSpec(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adruleevaluationspec_server = mcp
