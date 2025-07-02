"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeAdDisclaimerField = Literal["text", "title", "url"]


class AdCreativeAdDisclaimerFields(BaseModel):
    """Pydantic model for AdCreativeAdDisclaimer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    text: str = Field(None, alias="text")
    title: str = Field(None, alias="title")
    url: str = Field(None, alias="url")
