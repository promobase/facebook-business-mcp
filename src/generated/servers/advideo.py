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
async def create_advideo(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_cap_t_i_on_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_cap_t_i_on(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_collaborator_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_collaborator(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_comment_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_gaming_clip_create_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_gaming_clip_create(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_poll_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_poll(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_thumbnail_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).create_thumbnail(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_boost_ads_list_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_boost_ads_list(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_captions_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_captions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborators_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_collaborators(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crosspost_shared_pages_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_crosspost_shared_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_poll_settings_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_poll_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_polls_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_polls(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_thumbnails_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_thumbnails(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_video_insights_for_advideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdVideo(fbid=object_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
advideo_server = mcp
