"""
Auto-generated MCP server for Facebook PagePostExperiment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepostexperiment import PagePostExperiment
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepostexperiment")


# CRUD Operations


@mcp.tool()
async def api_create_pagepostexperiment(
    pagepostexperiment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagepostexperiment(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagepostexperiment(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagepostexperiment(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePostExperiment(fbid=pagepostexperiment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_video_insights(
    pagepostexperiment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePostExperiment(fbid=pagepostexperiment_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepostexperiment_server = mcp
