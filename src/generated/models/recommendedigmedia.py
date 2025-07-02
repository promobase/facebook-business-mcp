"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RecommendedIGMediaField = Literal["intent_score"]


class RecommendedIGMediaFields(BaseModel):
    """Pydantic model for RecommendedIGMedia fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    intent_score: float = Field(None, alias="intent_score")
