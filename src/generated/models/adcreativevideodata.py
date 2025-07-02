"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativecollectionthumbnailinfo import AdCreativeCollectionThumbnailInfoFields
    from .adcreativelinkdatacalltoaction import AdCreativeLinkDataCallToActionFields
    from .adcreativepostclickconfiguration import AdCreativePostClickConfigurationFields
    from .adcustomizationrulespec import AdCustomizationRuleSpecFields
    from .targeting import TargetingFields


# Field literal type
AdCreativeVideoDataField = Literal[
    "additional_image_index",
    "branded_content_shared_to_sponsor_status",
    "branded_content_sponsor_page_id",
    "call_to_action",
    "collection_thumbnails",
    "customization_rules_spec",
    "image_hash",
    "image_url",
    "link_description",
    "message",
    "offer_id",
    "page_welcome_message",
    "post_click_configuration",
    "retailer_item_ids",
    "targeting",
    "title",
    "video_id",
]


class AdCreativeVideoDataFields(BaseModel):
    """Pydantic model for AdCreativeVideoData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_image_index: int = Field(None, alias="additional_image_index")
    branded_content_shared_to_sponsor_status: str = Field(
        None, alias="branded_content_shared_to_sponsor_status"
    )
    branded_content_sponsor_page_id: str = Field(None, alias="branded_content_sponsor_page_id")
    call_to_action: AdCreativeLinkDataCallToActionFields = Field(None, alias="call_to_action")
    collection_thumbnails: list[AdCreativeCollectionThumbnailInfoFields] = Field(
        None, alias="collection_thumbnails"
    )
    customization_rules_spec: list[AdCustomizationRuleSpecFields] = Field(
        None, alias="customization_rules_spec"
    )
    image_hash: str = Field(None, alias="image_hash")
    image_url: str = Field(None, alias="image_url")
    link_description: str = Field(None, alias="link_description")
    message: str = Field(None, alias="message")
    offer_id: str = Field(None, alias="offer_id")
    page_welcome_message: str = Field(None, alias="page_welcome_message")
    post_click_configuration: AdCreativePostClickConfigurationFields = Field(
        None, alias="post_click_configuration"
    )
    retailer_item_ids: list[str] = Field(None, alias="retailer_item_ids")
    targeting: TargetingFields = Field(None, alias="targeting")
    title: str = Field(None, alias="title")
    video_id: str = Field(None, alias="video_id")
