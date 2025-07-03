"""
Auto-generated MCP server for Facebook CalibratorExistingRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.calibratorexistingrule import CalibratorExistingRule
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-calibratorexistingrule")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    calibratorexistingrule_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CalibratorExistingRule(fbid=calibratorexistingrule_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    calibratorexistingrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CalibratorExistingRule(fbid=calibratorexistingrule_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    calibratorexistingrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CalibratorExistingRule(fbid=calibratorexistingrule_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    calibratorexistingrule_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CalibratorExistingRule(fbid=calibratorexistingrule_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
calibratorexistingrule_server = mcp
