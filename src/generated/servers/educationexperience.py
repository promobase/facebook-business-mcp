"""
Auto-generated MCP server for Facebook EducationExperience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.educationexperience import EducationExperience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-educationexperience")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    educationexperience_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EducationExperience(fbid=educationexperience_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    educationexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EducationExperience(fbid=educationexperience_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    educationexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EducationExperience(fbid=educationexperience_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    educationexperience_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EducationExperience(fbid=educationexperience_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
educationexperience_server = mcp
