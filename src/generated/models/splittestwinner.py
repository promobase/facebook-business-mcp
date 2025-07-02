"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SplitTestWinnerField = Literal["ad_object_level", "confidences", "winner_ad_object_id"]


class SplitTestWinnerFields(BaseModel):
    """Pydantic model for SplitTestWinner fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_object_level: str = Field(None, alias="ad_object_level")
    confidences: list[dict[str, float]] = Field(None, alias="confidences")
    winner_ad_object_id: str = Field(None, alias="winner_ad_object_id")
