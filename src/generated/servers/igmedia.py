"""IGMedia MCP Server with typed wrappers."""

from facebook_business.adobjects.igmedia import IGMedia
from fastmcp import FastMCP

from src.generated.models.brandedcontentshadowiguserid import BrandedContentShadowIGUserIDField
from src.generated.models.igcomment import IGCommentField
from src.generated.models.igmedia import (
    IGMediaCreateBrandedContentPartnerPromoteParams,
    IGMediaCreateCommentParams,
    IGMediaCreateProductTagParams,
    IGMediaField,
    IGMediaGetInsightsParams,
    IGMediaUpdateParams,
)
from src.generated.models.instagraminsightsresult import InstagramInsightsResultField
from src.generated.models.shadowigmediaproducttags import ShadowIGMediaProductTagsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGMedia"
instructions = """
IGMedia MCP Server for Facebook Business API.

Provides typed access to all IGMedia operations.
"""

igmedia_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igmedia_server.tool
@wrapped_fn_tool
def get_igmedia(
    igmedia_id: str,
    fields: list[IGMediaField] = [],
) -> str:
    """Get a IGMedia object by ID.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to retrieve. Available fields: See IGMediaField type.
    """
    obj = IGMedia(igmedia_id)
    return obj.api_get(fields=fields)


@igmedia_server.tool
@wrapped_fn_tool
def update_igmedia(
    igmedia_id: str,
    fields: list[IGMediaField] = [],
    params: IGMediaUpdateParams | dict = {},
) -> str:
    """Update a IGMedia object.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to return after update. Available fields: See IGMediaField type.
        params: Parameters to update. Available params: See IGMediaUpdateParams type.
    """
    return IGMedia(igmedia_id).api_update(fields=fields, params=params)


# ---- Edge Methods (4) ----
@igmedia_server.tool
@wrapped_fn_tool
def create_branded_content_partner_promote(
    igmedia_id: str,
    fields: list[str] = [],
    params: IGMediaCreateBrandedContentPartnerPromoteParams | dict = {},
):
    """Create Branded Content Partner Promote for this IGMedia.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGMediaCreateBrandedContentPartnerPromoteParams type.
    """
    return IGMedia(igmedia_id).create_branded_content_partner_promote(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_comment(
    igmedia_id: str,
    fields: list[str] = [],
    params: IGMediaCreateCommentParams | dict = {},
):
    """Create Comment for this IGMedia.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGMediaCreateCommentParams type.
    """
    return IGMedia(igmedia_id).create_comment(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_insights(
    igmedia_id: str,
    fields: list[InstagramInsightsResultField] = [],
    params: IGMediaGetInsightsParams | dict = {},
):
    """Get Insights for this IGMedia.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to retrieve. Available fields: See InstagramInsightsResultField type.
        params: Query parameters. Available params: See IGMediaGetInsightsParams type.
    """
    return IGMedia(igmedia_id).get_insights(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_product_tag(
    igmedia_id: str,
    fields: list[str] = [],
    params: IGMediaCreateProductTagParams | dict = {},
):
    """Create Product Tag for this IGMedia.

    Args:
        igmedia_id: The ID of the IGMedia.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGMediaCreateProductTagParams type.
    """
    return IGMedia(igmedia_id).create_product_tag(fields=fields, params=params)
