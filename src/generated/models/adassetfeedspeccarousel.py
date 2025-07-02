"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields
    from .adassetfeedspeccarouselchildattachment import AdAssetFeedSpecCarouselChildAttachmentFields


# Field literal type
AdAssetFeedSpecCarouselField = Literal[
    "adlabels", "child_attachments", "multi_share_end_card", "multi_share_optimized"
]


class AdAssetFeedSpecCarouselFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecCarousel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adlabels: list[AdAssetFeedSpecAssetLabelFields] = Field(None, alias="adlabels")
    child_attachments: list[AdAssetFeedSpecCarouselChildAttachmentFields] = Field(
        None, alias="child_attachments"
    )
    multi_share_end_card: bool = Field(None, alias="multi_share_end_card")
    multi_share_optimized: bool = Field(None, alias="multi_share_optimized")
