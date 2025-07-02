"""
Auto-generated MCP server for Facebook SingleOwnerAdditionalProfile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.singleowneradditionalprofile import SingleOwnerAdditionalProfile
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-singleowneradditionalprofile")


# CRUD Operations


@mcp.tool()
async def api_create_singleowneradditionalprofile(
    singleowneradditionalprofile_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_singleowneradditionalprofile(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_singleowneradditionalprofile(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_singleowneradditionalprofile(
    singleowneradditionalprofile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SingleOwnerAdditionalProfile(fbid=singleowneradditionalprofile_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
singleowneradditionalprofile_server = mcp
