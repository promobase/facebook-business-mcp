"""
Auto-generated MCP server for Facebook JobOpening.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.jobopening import JobOpening
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-jobopening")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    jobopening_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = JobOpening(fbid=jobopening_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    jobopening_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = JobOpening(fbid=jobopening_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    jobopening_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = JobOpening(fbid=jobopening_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    jobopening_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = JobOpening(fbid=jobopening_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
jobopening_server = mcp
