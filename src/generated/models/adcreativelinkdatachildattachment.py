"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativelinkdatacalltoaction import AdCreativeLinkDataCallToActionFields
    from .adcreativeplacedata import AdCreativePlaceDataFields
    from .adsimagecrops import AdsImageCropsFields


# Field literal type
AdCreativeLinkDataChildAttachmentField = Literal[
    "call_to_action",
    "caption",
    "description",
    "image_crops",
    "image_hash",
    "link",
    "name",
    "picture",
    "place_data",
    "static_card",
    "video_id",
]


class AdCreativeLinkDataChildAttachmentFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataChildAttachment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    call_to_action: AdCreativeLinkDataCallToActionFields = Field(None, alias="call_to_action")
    caption: str = Field(None, alias="caption")
    description: str = Field(None, alias="description")
    image_crops: AdsImageCropsFields = Field(None, alias="image_crops")
    image_hash: str = Field(None, alias="image_hash")
    link: str = Field(None, alias="link")
    name: str = Field(None, alias="name")
    picture: str = Field(None, alias="picture")
    place_data: AdCreativePlaceDataFields = Field(None, alias="place_data")
    static_card: bool = Field(None, alias="static_card")
    video_id: str = Field(None, alias="video_id")
