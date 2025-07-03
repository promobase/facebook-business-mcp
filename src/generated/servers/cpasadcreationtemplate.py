"""
Auto-generated MCP server for Facebook CPASAdCreationTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasadcreationtemplate import CPASAdCreationTemplate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasadcreationtemplate")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    cpasadcreationtemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasadcreationtemplate_server = mcp
