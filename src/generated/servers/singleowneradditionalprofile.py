"""
Auto-generated MCP server for Facebook SingleOwnerAdditionalProfile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.singleowneradditionalprofile import SingleOwnerAdditionalProfile
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-singleowneradditionalprofile")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    singleowneradditionalprofile_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
singleowneradditionalprofile_server = mcp
