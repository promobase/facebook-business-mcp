"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
AdAccountAdVolumeField = Literal[
    "actor_id",
    "actor_name",
    "ad_limit_scope_business",
    "ad_limit_scope_business_manager_id",
    "ad_limit_set_by_page_admin",
    "ads_running_or_in_review_count",
    "ads_running_or_in_review_count_subject_to_limit_set_by_page",
    "current_account_ads_running_or_in_review_count",
    "future_limit_activation_date",
    "future_limit_on_ads_running_or_in_review",
    "limit_on_ads_running_or_in_review",
    "recommendations",
]


class AdAccountAdVolumeFields(BaseModel):
    """Pydantic model for AdAccountAdVolume fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actor_id: str = Field(None, alias="actor_id")
    actor_name: str = Field(None, alias="actor_name")
    ad_limit_scope_business: BusinessFields = Field(None, alias="ad_limit_scope_business")
    ad_limit_scope_business_manager_id: str = Field(
        None, alias="ad_limit_scope_business_manager_id"
    )
    ad_limit_set_by_page_admin: int = Field(None, alias="ad_limit_set_by_page_admin")
    ads_running_or_in_review_count: int = Field(None, alias="ads_running_or_in_review_count")
    ads_running_or_in_review_count_subject_to_limit_set_by_page: int = Field(
        None, alias="ads_running_or_in_review_count_subject_to_limit_set_by_page"
    )
    current_account_ads_running_or_in_review_count: int = Field(
        None, alias="current_account_ads_running_or_in_review_count"
    )
    future_limit_activation_date: str = Field(None, alias="future_limit_activation_date")
    future_limit_on_ads_running_or_in_review: int = Field(
        None, alias="future_limit_on_ads_running_or_in_review"
    )
    limit_on_ads_running_or_in_review: int = Field(None, alias="limit_on_ads_running_or_in_review")
    recommendations: list[dict[str, Any]] = Field(None, alias="recommendations")
