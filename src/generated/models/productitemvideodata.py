"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemVideoDataField = Literal["tags", "url"]


class ProductItemVideoDataFields(BaseModel):
    """Pydantic model for ProductItemVideoData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    tags: list[str] = Field(None, alias="tags")
    url: str = Field(None, alias="url")
