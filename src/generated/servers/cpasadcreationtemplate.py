"""
Auto-generated MCP server for Facebook CPASAdCreationTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasadcreationtemplate import CPASAdCreationTemplate
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasadcreationtemplate")


# CRUD Operations


@mcp.tool()
async def api_create_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CPASAdCreationTemplate(fbid=cpasadcreationtemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasadcreationtemplate_server = mcp
