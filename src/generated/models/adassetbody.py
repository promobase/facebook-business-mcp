"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAssetBodyField = Literal["id", "text", "url_tags"]


class AdAssetBodyFields(BaseModel):
    """Pydantic model for AdAssetBody fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    text: str = Field(None, alias="text")
    url_tags: str = Field(None, alias="url_tags")
