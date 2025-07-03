"""
Auto-generated MCP server for Facebook CPASParentCatalogSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasparentcatalogsettings import CPASParentCatalogSettings
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasparentcatalogsettings")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    cpasparentcatalogsettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASParentCatalogSettings(fbid=cpasparentcatalogsettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    cpasparentcatalogsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASParentCatalogSettings(fbid=cpasparentcatalogsettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    cpasparentcatalogsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASParentCatalogSettings(fbid=cpasparentcatalogsettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    cpasparentcatalogsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CPASParentCatalogSettings(fbid=cpasparentcatalogsettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasparentcatalogsettings_server = mcp
