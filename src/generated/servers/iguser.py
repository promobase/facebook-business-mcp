"""IGUser MCP Server with typed wrappers."""

from facebook_business.adobjects.iguser import IGUser
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.brandedcontentshadowigmediaid import BrandedContentShadowIGMediaIDField
from src.generated.models.brandedcontentshadowiguserid import BrandedContentShadowIGUserIDField
from src.generated.models.contentpublishinglimitresponse import ContentPublishingLimitResponseField
from src.generated.models.dataset import DatasetField
from src.generated.models.igbcadspermission import IGBCAdsPermissionField
from src.generated.models.igmedia import IGMediaField
from src.generated.models.igshoppingproductappeal import IGShoppingProductAppealField
from src.generated.models.iguser import (
    IGUserCreateAuthorizedAdAccountParams,
    IGUserCreateBrandedContentAdPermissionParams,
    IGUserCreateBrandedContentTagApprovalParams,
    IGUserCreateDatasetParams,
    IGUserCreateMediaParams,
    IGUserCreateMediaPublishParams,
    IGUserCreateMentionParams,
    IGUserCreateProductAppealParams,
    IGUserCreateUpcomingEventParams,
    IGUserDeleteBrandedContentTagApprovalParams,
    IGUserField,
    IGUserGetAuthorizedAdAccountsParams,
    IGUserGetBrandedContentAdvertisableMediasParams,
    IGUserGetBrandedContentTagApprovalParams,
    IGUserGetCatalogProductSearchParams,
    IGUserGetContentPublishingLimitParams,
    IGUserGetInsightsParams,
    IGUserGetLiveMediaParams,
    IGUserGetMediaParams,
    IGUserGetProductAppealParams,
    IGUserGetWelcomeMessageFlowsParams,
)
from src.generated.models.instagraminsightsresult import InstagramInsightsResultField
from src.generated.models.shadowigusercatalogproductsearch import (
    ShadowIGUserCatalogProductSearchField,
)
from src.generated.models.shadowiguserctxpartnerappwelcomemessageflow import (
    ShadowIGUserCTXPartnerAppWelcomeMessageFlowField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUser"
instructions = """
IGUser MCP Server for Facebook Business API.

Provides typed access to all IGUser operations.
"""

iguser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguser_server.tool
@wrapped_fn_tool
def get_iguser(
    iguser_id: str,
    fields: list[IGUserField] = [],
) -> str:
    """Get a IGUser object by ID.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See IGUserField type.
    """
    obj = IGUser(iguser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (20) ----
@iguser_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    iguser_id: str,
    fields: list[AdAccountField] = [],
    params: IGUserGetAuthorizedAdAccountsParams | dict = {},
):
    """Get Authorized Ad Accounts for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See IGUserGetAuthorizedAdAccountsParams type.
    """
    return IGUser(iguser_id).get_authorized_ad_accounts(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_authorized_ad_account(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateAuthorizedAdAccountParams | dict = {},
):
    """Create Authorized Ad Account for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateAuthorizedAdAccountParams type.
    """
    return IGUser(iguser_id).create_authorized_ad_account(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_branded_content_ad_permission(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateBrandedContentAdPermissionParams | dict = {},
):
    """Create Branded Content Ad Permission for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateBrandedContentAdPermissionParams type.
    """
    return IGUser(iguser_id).create_branded_content_ad_permission(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_branded_content_advertisable_medias(
    iguser_id: str,
    fields: list[BrandedContentShadowIGMediaIDField] = [],
    params: IGUserGetBrandedContentAdvertisableMediasParams | dict = {},
):
    """Get Branded Content Advertisable Medias for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See BrandedContentShadowIGMediaIDField type.
        params: Query parameters. Available params: See IGUserGetBrandedContentAdvertisableMediasParams type.
    """
    return IGUser(iguser_id).get_branded_content_advertisable_medias(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def delete_branded_content_tag_approval(
    iguser_id: str,
    params: IGUserDeleteBrandedContentTagApprovalParams | dict = {},
):
    """Delete Branded Content Tag Approval for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        params: Query parameters. Available params: See IGUserDeleteBrandedContentTagApprovalParams type.
    """
    return IGUser(iguser_id).delete_branded_content_tag_approval(params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_branded_content_tag_approval(
    iguser_id: str,
    fields: list[BrandedContentShadowIGUserIDField] = [],
    params: IGUserGetBrandedContentTagApprovalParams | dict = {},
):
    """Get Branded Content Tag Approval for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See BrandedContentShadowIGUserIDField type.
        params: Query parameters. Available params: See IGUserGetBrandedContentTagApprovalParams type.
    """
    return IGUser(iguser_id).get_branded_content_tag_approval(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateBrandedContentTagApprovalParams | dict = {},
):
    """Create Branded Content Tag Approval for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateBrandedContentTagApprovalParams type.
    """
    return IGUser(iguser_id).create_branded_content_tag_approval(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_catalog_product_search(
    iguser_id: str,
    fields: list[ShadowIGUserCatalogProductSearchField] = [],
    params: IGUserGetCatalogProductSearchParams | dict = {},
):
    """Get Catalog Product Search for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See ShadowIGUserCatalogProductSearchField type.
        params: Query parameters. Available params: See IGUserGetCatalogProductSearchParams type.
    """
    return IGUser(iguser_id).get_catalog_product_search(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_content_publishing_limit(
    iguser_id: str,
    fields: list[ContentPublishingLimitResponseField] = [],
    params: IGUserGetContentPublishingLimitParams | dict = {},
):
    """Get Content Publishing Limit for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See ContentPublishingLimitResponseField type.
        params: Query parameters. Available params: See IGUserGetContentPublishingLimitParams type.
    """
    return IGUser(iguser_id).get_content_publishing_limit(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_dataset(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateDatasetParams | dict = {},
):
    """Create Dataset for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateDatasetParams type.
    """
    return IGUser(iguser_id).create_dataset(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_insights(
    iguser_id: str,
    fields: list[InstagramInsightsResultField] = [],
    params: IGUserGetInsightsParams | dict = {},
):
    """Get Insights for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See InstagramInsightsResultField type.
        params: Query parameters. Available params: See IGUserGetInsightsParams type.
    """
    return IGUser(iguser_id).get_insights(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_live_media(
    iguser_id: str,
    fields: list[IGMediaField] = [],
    params: IGUserGetLiveMediaParams | dict = {},
):
    """Get Live Media for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See IGMediaField type.
        params: Query parameters. Available params: See IGUserGetLiveMediaParams type.
    """
    return IGUser(iguser_id).get_live_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_media(
    iguser_id: str,
    fields: list[IGMediaField] = [],
    params: IGUserGetMediaParams | dict = {},
):
    """Get Media for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See IGMediaField type.
        params: Query parameters. Available params: See IGUserGetMediaParams type.
    """
    return IGUser(iguser_id).get_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_media(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateMediaParams | dict = {},
):
    """Create Media for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateMediaParams type.
    """
    return IGUser(iguser_id).create_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_media_publish(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateMediaPublishParams | dict = {},
):
    """Create Media Publish for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateMediaPublishParams type.
    """
    return IGUser(iguser_id).create_media_publish(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_mention(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateMentionParams | dict = {},
):
    """Create Mention for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateMentionParams type.
    """
    return IGUser(iguser_id).create_mention(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_product_appeal(
    iguser_id: str,
    fields: list[IGShoppingProductAppealField] = [],
    params: IGUserGetProductAppealParams | dict = {},
):
    """Get Product Appeal for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See IGShoppingProductAppealField type.
        params: Query parameters. Available params: See IGUserGetProductAppealParams type.
    """
    return IGUser(iguser_id).get_product_appeal(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_product_appeal(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateProductAppealParams | dict = {},
):
    """Create Product Appeal for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateProductAppealParams type.
    """
    return IGUser(iguser_id).create_product_appeal(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_upcoming_event(
    iguser_id: str,
    fields: list[str] = [],
    params: IGUserCreateUpcomingEventParams | dict = {},
):
    """Create Upcoming Event for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGUserCreateUpcomingEventParams type.
    """
    return IGUser(iguser_id).create_upcoming_event(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    iguser_id: str,
    fields: list[ShadowIGUserCTXPartnerAppWelcomeMessageFlowField] = [],
    params: IGUserGetWelcomeMessageFlowsParams | dict = {},
):
    """Get Welcome Message Flows for this IGUser.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve. Available fields: See ShadowIGUserCTXPartnerAppWelcomeMessageFlowField type.
        params: Query parameters. Available params: See IGUserGetWelcomeMessageFlowsParams type.
    """
    return IGUser(iguser_id).get_welcome_message_flows(fields=fields, params=params)
