"""
Auto-generated MCP server for Facebook AdRuleExecutionSpec.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adruleexecutionspec import AdRuleExecutionSpec
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adruleexecutionspec")


# CRUD Operations


@mcp.tool()
async def get_adruleexecutionspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdRuleExecutionSpec.

    Args:
        object_id: The ID of the AdRuleExecutionSpec
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdRuleExecutionSpec(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adruleexecutionspec_server = mcp
