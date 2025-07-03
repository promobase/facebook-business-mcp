"""
Auto-generated MCP server for Facebook PagePostExperiment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepostexperiment import PagePostExperiment
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepostexperiment")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    pagepostexperiment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_video_insights(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePostExperiment(fbid=pagepostexperiment_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepostexperiment_server = mcp
