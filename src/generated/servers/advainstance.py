"""
Auto-generated MCP server for Facebook AdvAInstance.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.advainstance import AdvAInstance
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-advainstance")


# CRUD Operations


@mcp.tool()
async def api_create_advainstance(
    advainstance_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdvAInstance(fbid=advainstance_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_advainstance(
    advainstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdvAInstance(fbid=advainstance_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_advainstance(
    advainstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdvAInstance(fbid=advainstance_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_advainstance(
    advainstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdvAInstance(fbid=advainstance_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
advainstance_server = mcp
