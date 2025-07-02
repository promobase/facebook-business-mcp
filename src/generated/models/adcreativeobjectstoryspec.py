"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativelinkdata import AdCreativeLinkDataFields
    from .adcreativephotodata import AdCreativePhotoDataFields
    from .adcreativeproductdata import AdCreativeProductDataFields
    from .adcreativetextdata import AdCreativeTextDataFields
    from .adcreativevideodata import AdCreativeVideoDataFields


# Field literal type
AdCreativeObjectStorySpecField = Literal[
    "instagram_user_id",
    "link_data",
    "page_id",
    "photo_data",
    "product_data",
    "template_data",
    "text_data",
    "video_data",
]


class AdCreativeObjectStorySpecFields(BaseModel):
    """Pydantic model for AdCreativeObjectStorySpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    instagram_user_id: str = Field(None, alias="instagram_user_id")
    link_data: AdCreativeLinkDataFields = Field(None, alias="link_data")
    page_id: str = Field(None, alias="page_id")
    photo_data: AdCreativePhotoDataFields = Field(None, alias="photo_data")
    product_data: list[AdCreativeProductDataFields] = Field(None, alias="product_data")
    template_data: AdCreativeLinkDataFields = Field(None, alias="template_data")
    text_data: AdCreativeTextDataFields = Field(None, alias="text_data")
    video_data: AdCreativeVideoDataFields = Field(None, alias="video_data")
