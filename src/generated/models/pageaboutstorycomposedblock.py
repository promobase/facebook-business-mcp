"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .pageaboutstorycomposedblockentityranges import (
        PageAboutStoryComposedBlockEntityRangesFields,
    )
    from .pageaboutstorycomposedblockinlinestyle import PageAboutStoryComposedBlockInlineStyleFields


# Field literal type
PageAboutStoryComposedBlockField = Literal[
    "depth", "entity_ranges", "inline_style_ranges", "text", "type"
]


class PageAboutStoryComposedBlockFields(BaseModel):
    """Pydantic model for PageAboutStoryComposedBlock fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    depth: int = Field(None, alias="depth")
    entity_ranges: list[PageAboutStoryComposedBlockEntityRangesFields] = Field(
        None, alias="entity_ranges"
    )
    inline_style_ranges: list[PageAboutStoryComposedBlockInlineStyleFields] = Field(
        None, alias="inline_style_ranges"
    )
    text: str = Field(None, alias="text")
    type: str = Field(None, alias="type")
