"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InsightsValueField = Literal[
    "campaign_id",
    "earning_source",
    "end_time",
    "engagement_source",
    "message_type",
    "messaging_channel",
    "monetization_tool",
    "recurring_notifications_entry_point",
    "recurring_notifications_frequency",
    "recurring_notifications_topic",
    "start_time",
    "value",
]


class InsightsValueFields(BaseModel):
    """Pydantic model for InsightsValue fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    campaign_id: str = Field(None, alias="campaign_id")
    earning_source: str = Field(None, alias="earning_source")
    end_time: datetime = Field(None, alias="end_time")
    engagement_source: str = Field(None, alias="engagement_source")
    message_type: str = Field(None, alias="message_type")
    messaging_channel: str = Field(None, alias="messaging_channel")
    monetization_tool: str = Field(None, alias="monetization_tool")
    recurring_notifications_entry_point: str = Field(
        None, alias="recurring_notifications_entry_point"
    )
    recurring_notifications_frequency: str = Field(None, alias="recurring_notifications_frequency")
    recurring_notifications_topic: str = Field(None, alias="recurring_notifications_topic")
    start_time: datetime = Field(None, alias="start_time")
    value: dict[str, Any] = Field(None, alias="value")
