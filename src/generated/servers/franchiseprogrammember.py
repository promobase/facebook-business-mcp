"""
Auto-generated MCP server for Facebook FranchiseProgramMember.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.franchiseprogrammember import FranchiseProgramMember
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-franchiseprogrammember")


# CRUD Operations


@mcp.tool()
async def api_create_franchiseprogrammember(
    franchiseprogrammember_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FranchiseProgramMember(fbid=franchiseprogrammember_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_franchiseprogrammember(
    franchiseprogrammember_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FranchiseProgramMember(fbid=franchiseprogrammember_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_franchiseprogrammember(
    franchiseprogrammember_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FranchiseProgramMember(fbid=franchiseprogrammember_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_franchiseprogrammember(
    franchiseprogrammember_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FranchiseProgramMember(fbid=franchiseprogrammember_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
franchiseprogrammember_server = mcp
