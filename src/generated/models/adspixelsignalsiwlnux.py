"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelSignalsIWLNuxField = Literal[
    "background_color", "content", "content_color", "content_size", "img_url"
]


class AdsPixelSignalsIWLNuxFields(BaseModel):
    """Pydantic model for AdsPixelSignalsIWLNux fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    background_color: str = Field(None, alias="background_color")
    content: str = Field(None, alias="content")
    content_color: str = Field(None, alias="content_color")
    content_size: str = Field(None, alias="content_size")
    img_url: str = Field(None, alias="img_url")
