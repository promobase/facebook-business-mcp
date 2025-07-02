"""
Auto-generated MCP server for Facebook IGMedia.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmedia import IGMedia
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igmedia")


# CRUD Operations


@mcp.tool()
async def get_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGMedia(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = IGMedia(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_branded_content_partner_promote_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Branded Content Partner Promote for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_branded_content_partner_promote result
    """
    result = IGMedia(fbid=object_id).create_branded_content_partner_promote(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_comment_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = IGMedia(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_partnership_ad_code_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Partnership Ad Code for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_partnership_ad_code result
    """
    result = IGMedia(fbid=object_id).create_partnership_ad_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_tag_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Tag for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_tag result
    """
    result = IGMedia(fbid=object_id).create_product_tag(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_partnership_ad_code_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Partnership Ad Code for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_partnership_ad_code result
    """
    result = IGMedia(fbid=object_id).delete_partnership_ad_code(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_boost_ads_list_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Boost Ads List for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_boost_ads_list result
    """
    result = IGMedia(fbid=object_id).get_boost_ads_list(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_partner_promote_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Branded Content Partner Promote for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_branded_content_partner_promote result
    """
    result = IGMedia(fbid=object_id).get_branded_content_partner_promote(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_children_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Children for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_children result
    """
    result = IGMedia(fbid=object_id).get_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborators_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Collaborators for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborators result
    """
    result = IGMedia(fbid=object_id).get_collaborators(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = IGMedia(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = IGMedia(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_tags_for_igmedia(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Tags for IGMedia.

    Args:
        object_id: The ID of the IGMedia
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_tags result
    """
    result = IGMedia(fbid=object_id).get_product_tags(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmedia_server = mcp
