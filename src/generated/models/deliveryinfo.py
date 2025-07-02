"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DeliveryInfoField = Literal[
    "active_accelerated_campaign_count",
    "active_day_parted_campaign_count",
    "ad_penalty_map",
    "are_all_daily_budgets_spent",
    "credit_needed_ads_count",
    "eligible_for_delivery_insights",
    "end_time",
    "has_account_hit_spend_limit",
    "has_campaign_group_hit_spend_limit",
    "has_no_active_ads",
    "has_no_ads",
    "inactive_ads_count",
    "inactive_campaign_count",
    "is_account_closed",
    "is_account_disabled",
    "is_ad_uneconomical",
    "is_adfarm_penalized",
    "is_adgroup_partially_rejected",
    "is_campaign_accelerated",
    "is_campaign_completed",
    "is_campaign_day_parted",
    "is_campaign_disabled",
    "is_campaign_group_disabled",
    "is_clickbait_penalized",
    "is_daily_budget_spent",
    "is_engagement_bait_penalized",
    "is_lqwe_penalized",
    "is_reach_and_frequency_misconfigured",
    "is_sensationalism_penalized",
    "is_split_test_active",
    "is_split_test_valid",
    "lift_study_time_period",
    "needs_credit",
    "needs_tax_number",
    "non_deleted_ads_count",
    "not_delivering_campaign_count",
    "pending_ads_count",
    "reach_frequency_campaign_underdelivery_reason",
    "rejected_ads_count",
    "start_time",
    "status",
    "text_penalty_level",
]


class DeliveryInfoFields(BaseModel):
    """Pydantic model for DeliveryInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active_accelerated_campaign_count: int = Field(None, alias="active_accelerated_campaign_count")
    active_day_parted_campaign_count: int = Field(None, alias="active_day_parted_campaign_count")
    ad_penalty_map: list[dict[str, bool]] = Field(None, alias="ad_penalty_map")
    are_all_daily_budgets_spent: bool = Field(None, alias="are_all_daily_budgets_spent")
    credit_needed_ads_count: int = Field(None, alias="credit_needed_ads_count")
    eligible_for_delivery_insights: bool = Field(None, alias="eligible_for_delivery_insights")
    end_time: datetime = Field(None, alias="end_time")
    has_account_hit_spend_limit: bool = Field(None, alias="has_account_hit_spend_limit")
    has_campaign_group_hit_spend_limit: bool = Field(
        None, alias="has_campaign_group_hit_spend_limit"
    )
    has_no_active_ads: bool = Field(None, alias="has_no_active_ads")
    has_no_ads: bool = Field(None, alias="has_no_ads")
    inactive_ads_count: int = Field(None, alias="inactive_ads_count")
    inactive_campaign_count: int = Field(None, alias="inactive_campaign_count")
    is_account_closed: bool = Field(None, alias="is_account_closed")
    is_account_disabled: bool = Field(None, alias="is_account_disabled")
    is_ad_uneconomical: bool = Field(None, alias="is_ad_uneconomical")
    is_adfarm_penalized: bool = Field(None, alias="is_adfarm_penalized")
    is_adgroup_partially_rejected: bool = Field(None, alias="is_adgroup_partially_rejected")
    is_campaign_accelerated: bool = Field(None, alias="is_campaign_accelerated")
    is_campaign_completed: bool = Field(None, alias="is_campaign_completed")
    is_campaign_day_parted: bool = Field(None, alias="is_campaign_day_parted")
    is_campaign_disabled: bool = Field(None, alias="is_campaign_disabled")
    is_campaign_group_disabled: bool = Field(None, alias="is_campaign_group_disabled")
    is_clickbait_penalized: bool = Field(None, alias="is_clickbait_penalized")
    is_daily_budget_spent: bool = Field(None, alias="is_daily_budget_spent")
    is_engagement_bait_penalized: bool = Field(None, alias="is_engagement_bait_penalized")
    is_lqwe_penalized: bool = Field(None, alias="is_lqwe_penalized")
    is_reach_and_frequency_misconfigured: bool = Field(
        None, alias="is_reach_and_frequency_misconfigured"
    )
    is_sensationalism_penalized: bool = Field(None, alias="is_sensationalism_penalized")
    is_split_test_active: bool = Field(None, alias="is_split_test_active")
    is_split_test_valid: bool = Field(None, alias="is_split_test_valid")
    lift_study_time_period: str = Field(None, alias="lift_study_time_period")
    needs_credit: bool = Field(None, alias="needs_credit")
    needs_tax_number: bool = Field(None, alias="needs_tax_number")
    non_deleted_ads_count: int = Field(None, alias="non_deleted_ads_count")
    not_delivering_campaign_count: int = Field(None, alias="not_delivering_campaign_count")
    pending_ads_count: int = Field(None, alias="pending_ads_count")
    reach_frequency_campaign_underdelivery_reason: str = Field(
        None, alias="reach_frequency_campaign_underdelivery_reason"
    )
    rejected_ads_count: int = Field(None, alias="rejected_ads_count")
    start_time: datetime = Field(None, alias="start_time")
    status: str = Field(None, alias="status")
    text_penalty_level: str = Field(None, alias="text_penalty_level")
