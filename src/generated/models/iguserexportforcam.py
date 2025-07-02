"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class iguserexportforcaminsights_metrics_enum_param(str, Enum):
    """iguserexportforcaminsights_metrics_enum_param enum values."""

    CREATOR_ENGAGED_ACCOUNTS = "CREATOR_ENGAGED_ACCOUNTS"
    CREATOR_REACH = "CREATOR_REACH"
    REELS_HOOK_RATE = "REELS_HOOK_RATE"
    REELS_INTERACTION_RATE = "REELS_INTERACTION_RATE"
    TOTAL_FOLLOWERS = "TOTAL_FOLLOWERS"


class iguserexportforcaminsights_time_range_enum_param(str, Enum):
    """iguserexportforcaminsights_time_range_enum_param enum values."""

    LAST_14_DAYS = "LAST_14_DAYS"
    LAST_90_DAYS = "LAST_90_DAYS"
    LIFETIME = "LIFETIME"
    THIS_MONTH = "THIS_MONTH"
    THIS_WEEK = "THIS_WEEK"


class iguserexportforcaminsights_period_enum_param(str, Enum):
    """iguserexportforcaminsights_period_enum_param enum values."""

    DAY = "DAY"
    OVERALL = "OVERALL"


class iguserexportforcaminsights_breakdown_enum_param(str, Enum):
    """iguserexportforcaminsights_breakdown_enum_param enum values."""

    AGE = "AGE"
    FOLLOW_TYPE = "FOLLOW_TYPE"
    GENDER = "GENDER"
    MEDIA_TYPE = "MEDIA_TYPE"
    TOP_CITIES = "TOP_CITIES"
    TOP_COUNTRIES = "TOP_COUNTRIES"


# Field literal type
IGUserExportForCAMField = Literal[
    "age_bucket",
    "biography",
    "country",
    "email",
    "gender",
    "id",
    "is_account_verified",
    "is_paid_partnership_messages_enabled",
    "messaging_id",
    "onboarded_status",
    "portfolio_url",
    "username",
]


class IGUserExportForCAMFields(BaseModel):
    """Pydantic model for IGUserExportForCAM fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    age_bucket: str = Field(None, alias="age_bucket")
    biography: str = Field(None, alias="biography")
    country: str = Field(None, alias="country")
    email: str = Field(None, alias="email")
    gender: str = Field(None, alias="gender")
    id: str = Field(None, alias="id")
    is_account_verified: bool = Field(None, alias="is_account_verified")
    is_paid_partnership_messages_enabled: bool = Field(
        None, alias="is_paid_partnership_messages_enabled"
    )
    messaging_id: str = Field(None, alias="messaging_id")
    onboarded_status: bool = Field(None, alias="onboarded_status")
    portfolio_url: str = Field(None, alias="portfolio_url")
    username: str = Field(None, alias="username")


class IGUserExportForCAMGetInsightsParams(BaseModel):
    """Parameters for IGUserExportForCAM.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: iguserexportforcaminsights_breakdown_enum_param | None = Field(
        None, description="breakdown parameter"
    )
    metrics: list[iguserexportforcaminsights_metrics_enum_param] | None = Field(
        None, description="metrics parameter"
    )
    period: iguserexportforcaminsights_period_enum_param | None = Field(
        None, description="period parameter"
    )
    time_range: iguserexportforcaminsights_time_range_enum_param | None = Field(
        None, description="time_range parameter"
    )
