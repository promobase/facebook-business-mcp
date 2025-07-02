"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageAboutStoryComposedBlockInlineStyleField = Literal["length", "offset", "style"]


class PageAboutStoryComposedBlockInlineStyleFields(BaseModel):
    """Pydantic model for PageAboutStoryComposedBlockInlineStyle fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    length: int = Field(None, alias="length")
    offset: int = Field(None, alias="offset")
    style: str = Field(None, alias="style")
