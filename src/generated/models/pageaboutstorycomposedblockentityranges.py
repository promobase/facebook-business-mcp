"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageAboutStoryComposedBlockEntityRangesField = Literal["key", "length", "offset"]


class PageAboutStoryComposedBlockEntityRangesFields(BaseModel):
    """Pydantic model for PageAboutStoryComposedBlockEntityRanges fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    key: str = Field(None, alias="key")
    length: int = Field(None, alias="length")
    offset: int = Field(None, alias="offset")
