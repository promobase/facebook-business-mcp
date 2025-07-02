"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelEventSuggestionRuleField = Literal[
    "7d_volume", "dismissed", "end_time", "event_type", "rank", "rule", "sample_urls", "start_time"
]


class AdsPixelEventSuggestionRuleFields(BaseModel):
    """Pydantic model for AdsPixelEventSuggestionRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field_7d_volume: int = Field(None, alias="7d_volume")
    dismissed: bool = Field(None, alias="dismissed")
    end_time: datetime = Field(None, alias="end_time")
    event_type: str = Field(None, alias="event_type")
    rank: int = Field(None, alias="rank")
    rule: str = Field(None, alias="rule")
    sample_urls: list[str] = Field(None, alias="sample_urls")
    start_time: datetime = Field(None, alias="start_time")
