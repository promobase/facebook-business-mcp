"""
Auto-generated MCP server for Facebook CollaborativeAdsShareSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.collaborativeadssharesettings import CollaborativeAdsShareSettings
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-collaborativeadssharesettings")


# CRUD Operations


@mcp.tool()
async def api_create_collaborativeadssharesettings(
    collaborativeadssharesettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CollaborativeAdsShareSettings(fbid=collaborativeadssharesettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_collaborativeadssharesettings(
    collaborativeadssharesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CollaborativeAdsShareSettings(fbid=collaborativeadssharesettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_collaborativeadssharesettings(
    collaborativeadssharesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CollaborativeAdsShareSettings(fbid=collaborativeadssharesettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_collaborativeadssharesettings(
    collaborativeadssharesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CollaborativeAdsShareSettings(fbid=collaborativeadssharesettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
collaborativeadssharesettings_server = mcp
