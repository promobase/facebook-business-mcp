"""
Auto-generated MCP server for Facebook CalibratorExistingRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.calibratorexistingrule import CalibratorExistingRule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-calibratorexistingrule")


# CRUD Operations


@mcp.tool()
async def get_calibratorexistingrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CalibratorExistingRule.

    Args:
        object_id: The ID of the CalibratorExistingRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CalibratorExistingRule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
calibratorexistingrule_server = mcp
