"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdActivity_event_type(str, Enum):
    """AdActivity_event_type enum values."""

    account_spending_limit_reached = "account_spending_limit_reached"
    ad_account_add_user_to_role = "ad_account_add_user_to_role"
    ad_account_billing_charge = "ad_account_billing_charge"
    ad_account_billing_charge_failed = "ad_account_billing_charge_failed"
    ad_account_billing_chargeback = "ad_account_billing_chargeback"
    ad_account_billing_chargeback_reversal = "ad_account_billing_chargeback_reversal"
    ad_account_billing_decline = "ad_account_billing_decline"
    ad_account_billing_refund = "ad_account_billing_refund"
    ad_account_remove_spend_limit = "ad_account_remove_spend_limit"
    ad_account_remove_user_from_role = "ad_account_remove_user_from_role"
    ad_account_reset_spend_limit = "ad_account_reset_spend_limit"
    ad_account_set_business_information = "ad_account_set_business_information"
    ad_account_update_audience_type_url_parameter = "ad_account_update_audience_type_url_parameter"
    ad_account_update_spend_limit = "ad_account_update_spend_limit"
    ad_account_update_status = "ad_account_update_status"
    ad_review_approved = "ad_review_approved"
    ad_review_declined = "ad_review_declined"
    adaccount_update_audience_segment = "adaccount_update_audience_segment"
    add_funding_source = "add_funding_source"
    add_images = "add_images"
    billing_event = "billing_event"
    campaign_ended = "campaign_ended"
    campaign_spending_limit_reached = "campaign_spending_limit_reached"
    conversion_event_updated = "conversion_event_updated"
    create_ad = "create_ad"
    create_ad_set = "create_ad_set"
    create_audience = "create_audience"
    create_campaign_group = "create_campaign_group"
    create_campaign_legacy = "create_campaign_legacy"
    delete_audience = "delete_audience"
    delete_images = "delete_images"
    di_ad_set_learning_stage_exit = "di_ad_set_learning_stage_exit"
    edit_and_update_ad_creative = "edit_and_update_ad_creative"
    edit_images = "edit_images"
    first_delivery_event = "first_delivery_event"
    funding_event_initiated = "funding_event_initiated"
    funding_event_successful = "funding_event_successful"
    lifetime_budget_spent = "lifetime_budget_spent"
    merge_campaigns = "merge_campaigns"
    receive_audience = "receive_audience"
    remove_funding_source = "remove_funding_source"
    remove_shared_audience = "remove_shared_audience"
    share_audience = "share_audience"
    unknown = "unknown"
    unshare_audience = "unshare_audience"
    update_ad_bid_info = "update_ad_bid_info"
    update_ad_bid_type = "update_ad_bid_type"
    update_ad_creative = "update_ad_creative"
    update_ad_friendly_name = "update_ad_friendly_name"
    update_ad_labels = "update_ad_labels"
    update_ad_run_status = "update_ad_run_status"
    update_ad_run_status_to_be_set_after_review = "update_ad_run_status_to_be_set_after_review"
    update_ad_set_ad_keywords = "update_ad_set_ad_keywords"
    update_ad_set_bid_adjustments = "update_ad_set_bid_adjustments"
    update_ad_set_bid_strategy = "update_ad_set_bid_strategy"
    update_ad_set_bidding = "update_ad_set_bidding"
    update_ad_set_budget = "update_ad_set_budget"
    update_ad_set_duration = "update_ad_set_duration"
    update_ad_set_learning_stage_status = "update_ad_set_learning_stage_status"
    update_ad_set_min_spend_target = "update_ad_set_min_spend_target"
    update_ad_set_name = "update_ad_set_name"
    update_ad_set_optimization_goal = "update_ad_set_optimization_goal"
    update_ad_set_run_status = "update_ad_set_run_status"
    update_ad_set_spend_cap = "update_ad_set_spend_cap"
    update_ad_set_target_spec = "update_ad_set_target_spec"
    update_ad_targets_spec = "update_ad_targets_spec"
    update_adgroup_stop_delivery = "update_adgroup_stop_delivery"
    update_audience = "update_audience"
    update_campaign_ad_scheduling = "update_campaign_ad_scheduling"
    update_campaign_budget = "update_campaign_budget"
    update_campaign_budget_optimization_toggling_status = (
        "update_campaign_budget_optimization_toggling_status"
    )
    update_campaign_budget_scheduling_state = "update_campaign_budget_scheduling_state"
    update_campaign_conversion_goal = "update_campaign_conversion_goal"
    update_campaign_delivery_destination = "update_campaign_delivery_destination"
    update_campaign_delivery_type = "update_campaign_delivery_type"
    update_campaign_group_ad_scheduling = "update_campaign_group_ad_scheduling"
    update_campaign_group_budget_scheduling_state = "update_campaign_group_budget_scheduling_state"
    update_campaign_group_delivery_type = "update_campaign_group_delivery_type"
    update_campaign_group_high_demand_periods = "update_campaign_group_high_demand_periods"
    update_campaign_group_spend_cap = "update_campaign_group_spend_cap"
    update_campaign_high_demand_periods = "update_campaign_high_demand_periods"
    update_campaign_name = "update_campaign_name"
    update_campaign_run_status = "update_campaign_run_status"
    update_campaign_schedule = "update_campaign_schedule"
    update_campaign_value_adjustment_rule = "update_campaign_value_adjustment_rule"
    update_delivery_type_cross_level_shift = "update_delivery_type_cross_level_shift"


# Field literal type
AdActivityField = Literal[
    "actor_id",
    "actor_name",
    "application_id",
    "application_name",
    "date_time_in_timezone",
    "event_time",
    "event_type",
    "extra_data",
    "object_id",
    "object_name",
    "object_type",
    "translated_event_type",
]


class AdActivityFields(BaseModel):
    """Pydantic model for AdActivity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actor_id: str = Field(None, alias="actor_id")
    actor_name: str = Field(None, alias="actor_name")
    application_id: str = Field(None, alias="application_id")
    application_name: str = Field(None, alias="application_name")
    date_time_in_timezone: str = Field(None, alias="date_time_in_timezone")
    event_time: datetime = Field(None, alias="event_time")
    event_type: dict[str, Any] = Field(None, alias="event_type")
    extra_data: str = Field(None, alias="extra_data")
    object_id: str = Field(None, alias="object_id")
    object_name: str = Field(None, alias="object_name")
    object_type: str = Field(None, alias="object_type")
    translated_event_type: str = Field(None, alias="translated_event_type")
