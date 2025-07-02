"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeFeatureCustomizationsField = Literal[
    "background_color",
    "catalog_feed_tag_name",
    "font_name",
    "image_crop_style",
    "pe_carousel",
    "showcase_card_display",
    "text_extraction",
    "text_style",
]


class AdCreativeFeatureCustomizationsFields(BaseModel):
    """Pydantic model for AdCreativeFeatureCustomizations fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    background_color: str = Field(None, alias="background_color")
    catalog_feed_tag_name: str = Field(None, alias="catalog_feed_tag_name")
    font_name: str = Field(None, alias="font_name")
    image_crop_style: str = Field(None, alias="image_crop_style")
    pe_carousel: dict[str, Any] = Field(None, alias="pe_carousel")
    showcase_card_display: str = Field(None, alias="showcase_card_display")
    text_extraction: dict[str, Any] = Field(None, alias="text_extraction")
    text_style: str = Field(None, alias="text_style")
