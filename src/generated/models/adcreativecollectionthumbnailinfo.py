"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adsimagecrops import AdsImageCropsFields


# Field literal type
AdCreativeCollectionThumbnailInfoField = Literal[
    "element_child_index", "element_crops", "element_id"
]


class AdCreativeCollectionThumbnailInfoFields(BaseModel):
    """Pydantic model for AdCreativeCollectionThumbnailInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    element_child_index: int = Field(None, alias="element_child_index")
    element_crops: AdsImageCropsFields = Field(None, alias="element_crops")
    element_id: str = Field(None, alias="element_id")
