"""
Auto-generated MCP server for Facebook RightsManagerDataExport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rightsmanagerdataexport import RightsManagerDataExport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-rightsmanagerdataexport")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    rightsmanagerdataexport_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RightsManagerDataExport(fbid=rightsmanagerdataexport_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    rightsmanagerdataexport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RightsManagerDataExport(fbid=rightsmanagerdataexport_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    rightsmanagerdataexport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RightsManagerDataExport(fbid=rightsmanagerdataexport_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    rightsmanagerdataexport_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RightsManagerDataExport(fbid=rightsmanagerdataexport_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rightsmanagerdataexport_server = mcp
