"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
EventRegistrationSettingField = Literal["id", "questions", "target_type", "ticket_tier_ids"]


class EventRegistrationSettingFields(BaseModel):
    """Pydantic model for EventRegistrationSetting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    questions: str = Field(None, alias="questions")
    target_type: str = Field(None, alias="target_type")
    ticket_tier_ids: list[str] = Field(None, alias="ticket_tier_ids")
