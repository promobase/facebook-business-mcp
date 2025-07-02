"""
Auto-generated MCP server for Facebook AudioIsrc.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audioisrc import AudioIsrc
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audioisrc")


# CRUD Operations


@mcp.tool()
async def api_create_audioisrc(
    audioisrc_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioIsrc(fbid=audioisrc_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_audioisrc(
    audioisrc_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioIsrc(fbid=audioisrc_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_audioisrc(
    audioisrc_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioIsrc(fbid=audioisrc_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_audioisrc(
    audioisrc_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AudioIsrc(fbid=audioisrc_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audioisrc_server = mcp
