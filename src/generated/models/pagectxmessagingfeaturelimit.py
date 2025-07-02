"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageCTXMessagingFeatureLimitField = Literal[
    "messaging_feature_limit_duration", "messaging_feature_limit_type", "messaging_violation_type"
]


class PageCTXMessagingFeatureLimitFields(BaseModel):
    """Pydantic model for PageCTXMessagingFeatureLimit fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    messaging_feature_limit_duration: int = Field(None, alias="messaging_feature_limit_duration")
    messaging_feature_limit_type: str = Field(None, alias="messaging_feature_limit_type")
    messaging_violation_type: str = Field(None, alias="messaging_violation_type")
