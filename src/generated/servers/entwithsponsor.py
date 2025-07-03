"""
Auto-generated MCP server for Facebook EntWithSponsor.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.entwithsponsor import EntWithSponsor
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-entwithsponsor")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    entwithsponsor_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EntWithSponsor(fbid=entwithsponsor_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    entwithsponsor_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EntWithSponsor(fbid=entwithsponsor_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    entwithsponsor_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EntWithSponsor(fbid=entwithsponsor_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    entwithsponsor_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EntWithSponsor(fbid=entwithsponsor_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
entwithsponsor_server = mcp
