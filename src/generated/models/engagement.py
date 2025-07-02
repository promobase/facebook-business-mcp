"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
EngagementField = Literal[
    "count",
    "count_string",
    "count_string_with_like",
    "count_string_without_like",
    "social_sentence",
    "social_sentence_with_like",
    "social_sentence_without_like",
]


class EngagementFields(BaseModel):
    """Pydantic model for Engagement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    count: int = Field(None, alias="count")
    count_string: str = Field(None, alias="count_string")
    count_string_with_like: str = Field(None, alias="count_string_with_like")
    count_string_without_like: str = Field(None, alias="count_string_without_like")
    social_sentence: str = Field(None, alias="social_sentence")
    social_sentence_with_like: str = Field(None, alias="social_sentence_with_like")
    social_sentence_without_like: str = Field(None, alias="social_sentence_without_like")
