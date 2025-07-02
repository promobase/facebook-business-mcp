"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativefeaturesspec import AdCreativeFeaturesSpecFields


# Field literal type
AdCreativeDegreesOfFreedomSpecField = Literal[
    "ad_handle_type",
    "creative_features_spec",
    "degrees_of_freedom_type",
    "image_transformation_types",
    "multi_media_transformation_type",
    "stories_transformation_types",
    "text_transformation_types",
    "video_transformation_types",
]


class AdCreativeDegreesOfFreedomSpecFields(BaseModel):
    """Pydantic model for AdCreativeDegreesOfFreedomSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_handle_type: str = Field(None, alias="ad_handle_type")
    creative_features_spec: AdCreativeFeaturesSpecFields = Field(
        None, alias="creative_features_spec"
    )
    degrees_of_freedom_type: str = Field(None, alias="degrees_of_freedom_type")
    image_transformation_types: list[str] = Field(None, alias="image_transformation_types")
    multi_media_transformation_type: str = Field(None, alias="multi_media_transformation_type")
    stories_transformation_types: list[str] = Field(None, alias="stories_transformation_types")
    text_transformation_types: list[str] = Field(None, alias="text_transformation_types")
    video_transformation_types: list[str] = Field(None, alias="video_transformation_types")
