"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MIXInsightsResultField = Literal[
    "daily_age_gender_breakdown",
    "daily_audio_library_values",
    "daily_ugc_values",
    "daily_values",
    "metric",
    "monthly_audio_library_values",
    "monthly_ugc_values",
    "monthly_values",
    "percent_growth",
    "shielded_fields",
    "total_age_gender_breakdown",
    "total_audio_library_value",
    "total_country_breakdown",
    "total_locale_breakdown",
    "total_product_breakdown",
    "total_ugc_value",
    "total_value",
    "trending_age",
    "trending_gender",
    "trending_interest",
    "trending_territory",
]


class MIXInsightsResultFields(BaseModel):
    """Pydantic model for MIXInsightsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    daily_age_gender_breakdown: list[dict[str, list[dict[str, int]]]] = Field(
        None, alias="daily_age_gender_breakdown"
    )
    daily_audio_library_values: list[dict[str, int]] = Field(
        None, alias="daily_audio_library_values"
    )
    daily_ugc_values: list[dict[str, int]] = Field(None, alias="daily_ugc_values")
    daily_values: list[dict[str, int]] = Field(None, alias="daily_values")
    metric: str = Field(None, alias="metric")
    monthly_audio_library_values: list[dict[str, int]] = Field(
        None, alias="monthly_audio_library_values"
    )
    monthly_ugc_values: list[dict[str, int]] = Field(None, alias="monthly_ugc_values")
    monthly_values: list[dict[str, int]] = Field(None, alias="monthly_values")
    percent_growth: float = Field(None, alias="percent_growth")
    shielded_fields: list[dict[str, list[dict[str, bool]]]] = Field(None, alias="shielded_fields")
    total_age_gender_breakdown: list[dict[str, int]] = Field(
        None, alias="total_age_gender_breakdown"
    )
    total_audio_library_value: int = Field(None, alias="total_audio_library_value")
    total_country_breakdown: list[dict[str, int]] = Field(None, alias="total_country_breakdown")
    total_locale_breakdown: list[dict[str, int]] = Field(None, alias="total_locale_breakdown")
    total_product_breakdown: list[dict[str, int]] = Field(None, alias="total_product_breakdown")
    total_ugc_value: int = Field(None, alias="total_ugc_value")
    total_value: int = Field(None, alias="total_value")
    trending_age: list[dict[str, list[dict[str, float]]]] = Field(None, alias="trending_age")
    trending_gender: list[dict[str, list[dict[str, float]]]] = Field(None, alias="trending_gender")
    trending_interest: list[dict[str, list[dict[str, float]]]] = Field(
        None, alias="trending_interest"
    )
    trending_territory: list[dict[str, list[dict[str, float]]]] = Field(
        None, alias="trending_territory"
    )
