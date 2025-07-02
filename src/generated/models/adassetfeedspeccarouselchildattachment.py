"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields


# Field literal type
AdAssetFeedSpecCarouselChildAttachmentField = Literal[
    "body_label",
    "call_to_action_type_label",
    "caption_label",
    "description_label",
    "image_label",
    "link_url_label",
    "phone_data_ids_label",
    "static_card",
    "title_label",
    "video_label",
]


class AdAssetFeedSpecCarouselChildAttachmentFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecCarouselChildAttachment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    body_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="body_label")
    call_to_action_type_label: AdAssetFeedSpecAssetLabelFields = Field(
        None, alias="call_to_action_type_label"
    )
    caption_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="caption_label")
    description_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="description_label")
    image_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="image_label")
    link_url_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="link_url_label")
    phone_data_ids_label: AdAssetFeedSpecAssetLabelFields = Field(
        None, alias="phone_data_ids_label"
    )
    static_card: bool = Field(None, alias="static_card")
    title_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="title_label")
    video_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="video_label")
