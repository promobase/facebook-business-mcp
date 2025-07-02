"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativecollectionthumbnailinfo import AdCreativeCollectionThumbnailInfoFields
    from .adcreativelinkdataapplinkspec import AdCreativeLinkDataAppLinkSpecFields
    from .adcreativelinkdatacalltoaction import AdCreativeLinkDataCallToActionFields
    from .adcreativelinkdatachildattachment import AdCreativeLinkDataChildAttachmentFields
    from .adcreativelinkdataimagelayerspec import AdCreativeLinkDataImageLayerSpecFields
    from .adcreativelinkdataimageoverlayspec import AdCreativeLinkDataImageOverlaySpecFields
    from .adcreativepostclickconfiguration import AdCreativePostClickConfigurationFields
    from .adcreativestaticfallbackspec import AdCreativeStaticFallbackSpecFields
    from .adcustomizationrulespec import AdCustomizationRuleSpecFields
    from .adsimagecrops import AdsImageCropsFields


class AdCreativeLinkData_format_option(str, Enum):
    """AdCreativeLinkData_format_option enum values."""

    carousel_ar_effects = "carousel_ar_effects"
    carousel_images_multi_items = "carousel_images_multi_items"
    carousel_images_single_item = "carousel_images_single_item"
    carousel_slideshows = "carousel_slideshows"
    collection_video = "collection_video"
    single_image = "single_image"


# Field literal type
AdCreativeLinkDataField = Literal[
    "ad_context",
    "additional_image_index",
    "app_link_spec",
    "attachment_style",
    "automated_product_tags",
    "boosted_product_set_id",
    "branded_content_shared_to_sponsor_status",
    "branded_content_sponsor_page_id",
    "call_to_action",
    "caption",
    "child_attachments",
    "collection_thumbnails",
    "customization_rules_spec",
    "description",
    "event_id",
    "force_single_link",
    "format_option",
    "image_crops",
    "image_hash",
    "image_layer_specs",
    "image_overlay_spec",
    "link",
    "message",
    "multi_share_end_card",
    "multi_share_optimized",
    "name",
    "offer_id",
    "page_welcome_message",
    "picture",
    "post_click_configuration",
    "preferred_image_tags",
    "preferred_video_tags",
    "retailer_item_ids",
    "show_multiple_images",
    "static_fallback_spec",
    "use_flexible_image_aspect_ratio",
]


class AdCreativeLinkDataFields(BaseModel):
    """Pydantic model for AdCreativeLinkData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_context: str = Field(None, alias="ad_context")
    additional_image_index: int = Field(None, alias="additional_image_index")
    app_link_spec: AdCreativeLinkDataAppLinkSpecFields = Field(None, alias="app_link_spec")
    attachment_style: str = Field(None, alias="attachment_style")
    automated_product_tags: bool = Field(None, alias="automated_product_tags")
    boosted_product_set_id: str = Field(None, alias="boosted_product_set_id")
    branded_content_shared_to_sponsor_status: str = Field(
        None, alias="branded_content_shared_to_sponsor_status"
    )
    branded_content_sponsor_page_id: str = Field(None, alias="branded_content_sponsor_page_id")
    call_to_action: AdCreativeLinkDataCallToActionFields = Field(None, alias="call_to_action")
    caption: str = Field(None, alias="caption")
    child_attachments: list[AdCreativeLinkDataChildAttachmentFields] = Field(
        None, alias="child_attachments"
    )
    collection_thumbnails: list[AdCreativeCollectionThumbnailInfoFields] = Field(
        None, alias="collection_thumbnails"
    )
    customization_rules_spec: list[AdCustomizationRuleSpecFields] = Field(
        None, alias="customization_rules_spec"
    )
    description: str = Field(None, alias="description")
    event_id: str = Field(None, alias="event_id")
    force_single_link: bool = Field(None, alias="force_single_link")
    format_option: dict[str, Any] = Field(None, alias="format_option")
    image_crops: AdsImageCropsFields = Field(None, alias="image_crops")
    image_hash: str = Field(None, alias="image_hash")
    image_layer_specs: list[AdCreativeLinkDataImageLayerSpecFields] = Field(
        None, alias="image_layer_specs"
    )
    image_overlay_spec: AdCreativeLinkDataImageOverlaySpecFields = Field(
        None, alias="image_overlay_spec"
    )
    link: str = Field(None, alias="link")
    message: str = Field(None, alias="message")
    multi_share_end_card: bool = Field(None, alias="multi_share_end_card")
    multi_share_optimized: bool = Field(None, alias="multi_share_optimized")
    name: str = Field(None, alias="name")
    offer_id: str = Field(None, alias="offer_id")
    page_welcome_message: str = Field(None, alias="page_welcome_message")
    picture: str = Field(None, alias="picture")
    post_click_configuration: AdCreativePostClickConfigurationFields = Field(
        None, alias="post_click_configuration"
    )
    preferred_image_tags: list[str] = Field(None, alias="preferred_image_tags")
    preferred_video_tags: list[str] = Field(None, alias="preferred_video_tags")
    retailer_item_ids: list[str] = Field(None, alias="retailer_item_ids")
    show_multiple_images: bool = Field(None, alias="show_multiple_images")
    static_fallback_spec: AdCreativeStaticFallbackSpecFields = Field(
        None, alias="static_fallback_spec"
    )
    use_flexible_image_aspect_ratio: bool = Field(None, alias="use_flexible_image_aspect_ratio")
