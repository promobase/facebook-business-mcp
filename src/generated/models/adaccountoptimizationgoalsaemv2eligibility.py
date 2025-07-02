"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdAccountOptimizationGoalsAEMv2Eligibility_optimization_goal(str, Enum):
    """AdAccountOptimizationGoalsAEMv2Eligibility_optimization_goal enum values."""

    ADVERTISER_SILOED_VALUE = "ADVERTISER_SILOED_VALUE"
    AD_RECALL_LIFT = "AD_RECALL_LIFT"
    APP_INSTALLS = "APP_INSTALLS"
    APP_INSTALLS_AND_OFFSITE_CONVERSIONS = "APP_INSTALLS_AND_OFFSITE_CONVERSIONS"
    CONVERSATIONS = "CONVERSATIONS"
    DERIVED_EVENTS = "DERIVED_EVENTS"
    ENGAGED_USERS = "ENGAGED_USERS"
    EVENT_RESPONSES = "EVENT_RESPONSES"
    IMPRESSIONS = "IMPRESSIONS"
    IN_APP_VALUE = "IN_APP_VALUE"
    LANDING_PAGE_VIEWS = "LANDING_PAGE_VIEWS"
    LEAD_GENERATION = "LEAD_GENERATION"
    LINK_CLICKS = "LINK_CLICKS"
    MEANINGFUL_CALL_ATTEMPT = "MEANINGFUL_CALL_ATTEMPT"
    MESSAGING_APPOINTMENT_CONVERSION = "MESSAGING_APPOINTMENT_CONVERSION"
    MESSAGING_PURCHASE_CONVERSION = "MESSAGING_PURCHASE_CONVERSION"
    NONE = "NONE"
    OFFSITE_CONVERSIONS = "OFFSITE_CONVERSIONS"
    PAGE_LIKES = "PAGE_LIKES"
    POST_ENGAGEMENT = "POST_ENGAGEMENT"
    PROFILE_AND_PAGE_ENGAGEMENT = "PROFILE_AND_PAGE_ENGAGEMENT"
    PROFILE_VISIT = "PROFILE_VISIT"
    QUALITY_CALL = "QUALITY_CALL"
    QUALITY_LEAD = "QUALITY_LEAD"
    REACH = "REACH"
    REMINDERS_SET = "REMINDERS_SET"
    SUBSCRIBERS = "SUBSCRIBERS"
    THRUPLAY = "THRUPLAY"
    VALUE = "VALUE"
    VISIT_INSTAGRAM_PROFILE = "VISIT_INSTAGRAM_PROFILE"


# Field literal type
AdAccountOptimizationGoalsAEMv2EligibilityField = Literal["is_disabled", "optimization_goal"]


class AdAccountOptimizationGoalsAEMv2EligibilityFields(BaseModel):
    """Pydantic model for AdAccountOptimizationGoalsAEMv2Eligibility fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_disabled: bool = Field(None, alias="is_disabled")
    optimization_goal: dict[str, Any] = Field(None, alias="optimization_goal")
