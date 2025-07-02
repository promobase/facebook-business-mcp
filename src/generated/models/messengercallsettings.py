"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessengerCallSettingsField = Literal["audio_enabled", "call_hours", "call_routing", "icon_enabled"]


class MessengerCallSettingsFields(BaseModel):
    """Pydantic model for MessengerCallSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_enabled: bool = Field(None, alias="audio_enabled")
    call_hours: dict[str, Any] = Field(None, alias="call_hours")
    call_routing: str = Field(None, alias="call_routing")
    icon_enabled: bool = Field(None, alias="icon_enabled")
