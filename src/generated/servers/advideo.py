"""
Auto-generated MCP server for Facebook AdVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.advideo import AdVideo
from facebook_business.api import FacebookAdsApi
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
    """
    Create a AdVideo.

    Args:
        object_id: The ID of the AdVideo
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
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
    """
    Delete a AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
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
    """
    Get a AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Cap T I On for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_cap_t_i_on result
    """
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
    """
    Create Collaborator for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_collaborator result
    """
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
    """
    Create Comment for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
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
    """
    Create Gaming Clip Create for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_gaming_clip_create result
    """
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
    """
    Create Like for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_like result
    """
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
    """
    Create Poll for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_poll result
    """
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
    """
    Create Thumbnail for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_thumbnail result
    """
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
    """
    Get Boost Ads List for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_boost_ads_list result
    """
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
    """
    Get Captions for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_captions result
    """
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
    """
    Get Collaborators for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborators result
    """
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
    """
    Get Comments for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
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
    """
    Get Crosspost Shared Pages for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_crosspost_shared_pages result
    """
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
    """
    Get Likes for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
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
    """
    Get Poll Settings for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_poll_settings result
    """
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
    """
    Get Polls for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_polls result
    """
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
    """
    Get Sponsor Tags for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sponsor_tags result
    """
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
    """
    Get Tags for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tags result
    """
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
    """
    Get Thumbnails for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_thumbnails result
    """
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
    """
    Get Video Insights for AdVideo.

    Args:
        object_id: The ID of the AdVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_insights result
    """
    result = AdVideo(fbid=object_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
advideo_server = mcp
