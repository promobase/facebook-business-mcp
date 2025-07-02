"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserNotificationSeenStateDataField = Literal["id", "seen_state"]


class UserNotificationSeenStateDataFields(BaseModel):
    """Pydantic model for UserNotificationSeenStateData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    seen_state: str = Field(None, alias="seen_state")
