"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserPageOneTimeOptInTokenSettingsField = Literal[
    "creation_timestamp",
    "next_eligible_time",
    "notification_messages_frequency",
    "notification_messages_reoptin",
    "notification_messages_timezone",
    "notification_messages_token",
    "recipient_id",
    "token_expiry_timestamp",
    "topic_title",
    "user_token_status",
]


class UserPageOneTimeOptInTokenSettingsFields(BaseModel):
    """Pydantic model for UserPageOneTimeOptInTokenSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_timestamp: int = Field(None, alias="creation_timestamp")
    next_eligible_time: int = Field(None, alias="next_eligible_time")
    notification_messages_frequency: str = Field(None, alias="notification_messages_frequency")
    notification_messages_reoptin: str = Field(None, alias="notification_messages_reoptin")
    notification_messages_timezone: str = Field(None, alias="notification_messages_timezone")
    notification_messages_token: str = Field(None, alias="notification_messages_token")
    recipient_id: str = Field(None, alias="recipient_id")
    token_expiry_timestamp: int = Field(None, alias="token_expiry_timestamp")
    topic_title: str = Field(None, alias="topic_title")
    user_token_status: str = Field(None, alias="user_token_status")
