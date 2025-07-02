"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OffsitePixelField = Literal["creator", "id", "js_pixel", "last_firing_time", "name", "tag"]


class OffsitePixelFields(BaseModel):
    """Pydantic model for OffsitePixel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creator: str = Field(None, alias="creator")
    id: str = Field(None, alias="id")
    js_pixel: str = Field(None, alias="js_pixel")
    last_firing_time: datetime = Field(None, alias="last_firing_time")
    name: str = Field(None, alias="name")
    tag: str = Field(None, alias="tag")
