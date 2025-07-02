"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetcustomizationrulecustomizationspec import (
        AdAssetCustomizationRuleCustomizationSpecFields,
    )
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields


# Field literal type
AdAssetFeedSpecAssetCustomizationRuleField = Literal[
    "body_label",
    "call_to_action_label",
    "call_to_action_type_label",
    "caption_label",
    "carousel_label",
    "customization_spec",
    "description_label",
    "image_label",
    "is_default",
    "link_url_label",
    "priority",
    "title_label",
    "video_label",
]


class AdAssetFeedSpecAssetCustomizationRuleFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecAssetCustomizationRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    body_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="body_label")
    call_to_action_label: AdAssetFeedSpecAssetLabelFields = Field(
        None, alias="call_to_action_label"
    )
    call_to_action_type_label: AdAssetFeedSpecAssetLabelFields = Field(
        None, alias="call_to_action_type_label"
    )
    caption_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="caption_label")
    carousel_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="carousel_label")
    customization_spec: AdAssetCustomizationRuleCustomizationSpecFields = Field(
        None, alias="customization_spec"
    )
    description_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="description_label")
    image_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="image_label")
    is_default: bool = Field(None, alias="is_default")
    link_url_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="link_url_label")
    priority: int = Field(None, alias="priority")
    title_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="title_label")
    video_label: AdAssetFeedSpecAssetLabelFields = Field(None, alias="video_label")
