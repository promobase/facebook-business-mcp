"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DynamicARMetadataField = Literal[
    "anchor_point",
    "container_effect_enum",
    "effect_icon_url",
    "effect_id",
    "id",
    "platforms",
    "scale_factor",
    "shadow_texture_url",
    "source_url",
    "state",
    "tags",
    "variant_picker_url",
]


class DynamicARMetadataFields(BaseModel):
    """Pydantic model for DynamicARMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    anchor_point: list[float] = Field(None, alias="anchor_point")
    container_effect_enum: int = Field(None, alias="container_effect_enum")
    effect_icon_url: str = Field(None, alias="effect_icon_url")
    effect_id: str = Field(None, alias="effect_id")
    id: str = Field(None, alias="id")
    platforms: list[str] = Field(None, alias="platforms")
    scale_factor: list[float] = Field(None, alias="scale_factor")
    shadow_texture_url: str = Field(None, alias="shadow_texture_url")
    source_url: str = Field(None, alias="source_url")
    state: str = Field(None, alias="state")
    tags: list[str] = Field(None, alias="tags")
    variant_picker_url: str = Field(None, alias="variant_picker_url")
