"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelCAPIIntegrationQualityField = Literal[
    "acr",
    "data_freshness",
    "dedupe_key_feedback",
    "event_coverage",
    "event_match_quality",
    "event_name",
    "event_potential_aly_acr_increase",
]


class AdsPixelCAPIIntegrationQualityFields(BaseModel):
    """Pydantic model for AdsPixelCAPIIntegrationQuality fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    acr: dict[str, Any] = Field(None, alias="acr")
    data_freshness: dict[str, Any] = Field(None, alias="data_freshness")
    dedupe_key_feedback: list[dict[str, Any]] = Field(None, alias="dedupe_key_feedback")
    event_coverage: dict[str, Any] = Field(None, alias="event_coverage")
    event_match_quality: dict[str, Any] = Field(None, alias="event_match_quality")
    event_name: str = Field(None, alias="event_name")
    event_potential_aly_acr_increase: dict[str, Any] = Field(
        None, alias="event_potential_aly_acr_increase"
    )
