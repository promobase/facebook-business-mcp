"""
Auto-generated MCP server for Facebook AdVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.advideo import AdVideo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-advideo")


# CRUD Operations


@mcp.tool()
async def api_create_advideo(
    advideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_advideo(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_advideo(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_advideo(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_cap_t_i_on(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_cap_t_i_on(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_collaborator(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_collaborator(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_comment(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_gaming_clip_create(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_gaming_clip_create(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_poll(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_poll(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_thumbnail(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).create_thumbnail(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_boost_ads_list(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_boost_ads_list(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_captions(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_captions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborators(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_collaborators(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crosspost_shared_pages(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_crosspost_shared_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_poll_settings(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_poll_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_polls(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_polls(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_thumbnails(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_thumbnails(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_insights(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=advideo_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
advideo_server = mcp
