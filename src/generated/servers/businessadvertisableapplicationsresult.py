"""
Auto-generated MCP server for Facebook BusinessAdvertisableApplicationsResult.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessadvertisableapplicationsresult import (
    BusinessAdvertisableApplicationsResult,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessadvertisableapplicationsresult")


# CRUD Operations


@mcp.tool()
async def api_create_businessadvertisableapplicationsresult(
    businessadvertisableapplicationsresult_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAdvertisableApplicationsResult(
        fbid=businessadvertisableapplicationsresult_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessadvertisableapplicationsresult(
    businessadvertisableapplicationsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAdvertisableApplicationsResult(
        fbid=businessadvertisableapplicationsresult_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessadvertisableapplicationsresult(
    businessadvertisableapplicationsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAdvertisableApplicationsResult(
        fbid=businessadvertisableapplicationsresult_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessadvertisableapplicationsresult(
    businessadvertisableapplicationsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessAdvertisableApplicationsResult(
        fbid=businessadvertisableapplicationsresult_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessadvertisableapplicationsresult_server = mcp
