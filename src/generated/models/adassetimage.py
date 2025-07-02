"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adsimagecrops import AdsImageCropsFields


# Field literal type
AdAssetImageField = Literal["hash", "id", "image_crops", "name", "tag", "url", "url_tags"]


class AdAssetImageFields(BaseModel):
    """Pydantic model for AdAssetImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    hash: str = Field(None, alias="hash")
    id: str = Field(None, alias="id")
    image_crops: AdsImageCropsFields = Field(None, alias="image_crops")
    name: str = Field(None, alias="name")
    tag: str = Field(None, alias="tag")
    url: str = Field(None, alias="url")
    url_tags: str = Field(None, alias="url_tags")
