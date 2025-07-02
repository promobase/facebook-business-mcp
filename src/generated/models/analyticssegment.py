"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsSegmentField = Literal[
    "custom_audience_ineligiblity_reasons",
    "description",
    "estimated_custom_audience_size",
    "event_info_rules",
    "event_rules",
    "filter_set",
    "has_demographic_rules",
    "id",
    "is_all_user",
    "is_eligible_for_push_campaign",
    "is_internal",
    "name",
    "percentile_rules",
    "time_last_seen",
    "time_last_updated",
    "user_property_rules",
    "web_param_rules",
]


class AnalyticsSegmentFields(BaseModel):
    """Pydantic model for AnalyticsSegment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_audience_ineligiblity_reasons: list[str] = Field(
        None, alias="custom_audience_ineligiblity_reasons"
    )
    description: str = Field(None, alias="description")
    estimated_custom_audience_size: int = Field(None, alias="estimated_custom_audience_size")
    event_info_rules: list[dict[str, Any]] = Field(None, alias="event_info_rules")
    event_rules: list[dict[str, Any]] = Field(None, alias="event_rules")
    filter_set: str = Field(None, alias="filter_set")
    has_demographic_rules: bool = Field(None, alias="has_demographic_rules")
    id: str = Field(None, alias="id")
    is_all_user: bool = Field(None, alias="is_all_user")
    is_eligible_for_push_campaign: bool = Field(None, alias="is_eligible_for_push_campaign")
    is_internal: bool = Field(None, alias="is_internal")
    name: str = Field(None, alias="name")
    percentile_rules: list[dict[str, Any]] = Field(None, alias="percentile_rules")
    time_last_seen: int = Field(None, alias="time_last_seen")
    time_last_updated: int = Field(None, alias="time_last_updated")
    user_property_rules: list[dict[str, Any]] = Field(None, alias="user_property_rules")
    web_param_rules: list[dict[str, Any]] = Field(None, alias="web_param_rules")
