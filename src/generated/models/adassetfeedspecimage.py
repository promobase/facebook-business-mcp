"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields
    from .adsimagecrops import AdsImageCropsFields


# Field literal type
AdAssetFeedSpecImageField = Literal["adlabels", "hash", "image_crops", "url", "url_tags"]


class AdAssetFeedSpecImageFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adlabels: list[AdAssetFeedSpecAssetLabelFields] = Field(None, alias="adlabels")
    hash: str = Field(None, alias="hash")
    image_crops: AdsImageCropsFields = Field(None, alias="image_crops")
    url: str = Field(None, alias="url")
    url_tags: str = Field(None, alias="url_tags")
