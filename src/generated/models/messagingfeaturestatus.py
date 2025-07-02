"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessagingFeatureStatusField = Literal["hop_v2", "ig_multi_app", "msgr_multi_app"]


class MessagingFeatureStatusFields(BaseModel):
    """Pydantic model for MessagingFeatureStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    hop_v2: bool = Field(None, alias="hop_v2")
    ig_multi_app: bool = Field(None, alias="ig_multi_app")
    msgr_multi_app: bool = Field(None, alias="msgr_multi_app")
