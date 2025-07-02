"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdVolumeField = Literal[
    "ad_volume_break_down",
    "ads_running_or_in_review_count",
    "future_limit_activation_date",
    "future_limit_on_ads_running_or_in_review",
    "individual_accounts_ad_volume",
    "is_gpa_page",
    "limit_on_ads_running_or_in_review",
    "owning_business_ad_volume",
    "partner_business_ad_volume",
    "user_role",
]


class AdVolumeFields(BaseModel):
    """Pydantic model for AdVolume fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_volume_break_down: list[dict[str, Any]] = Field(None, alias="ad_volume_break_down")
    ads_running_or_in_review_count: int = Field(None, alias="ads_running_or_in_review_count")
    future_limit_activation_date: str = Field(None, alias="future_limit_activation_date")
    future_limit_on_ads_running_or_in_review: int = Field(
        None, alias="future_limit_on_ads_running_or_in_review"
    )
    individual_accounts_ad_volume: int = Field(None, alias="individual_accounts_ad_volume")
    is_gpa_page: bool = Field(None, alias="is_gpa_page")
    limit_on_ads_running_or_in_review: int = Field(None, alias="limit_on_ads_running_or_in_review")
    owning_business_ad_volume: int = Field(None, alias="owning_business_ad_volume")
    partner_business_ad_volume: int = Field(None, alias="partner_business_ad_volume")
    user_role: str = Field(None, alias="user_role")
