"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAssetFeedAdditionalDataPageNudgeMessageField = Literal["enabled", "quick_replies", "text"]


class AdAssetFeedAdditionalDataPageNudgeMessageFields(BaseModel):
    """Pydantic model for AdAssetFeedAdditionalDataPageNudgeMessage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    enabled: bool = Field(None, alias="enabled")
    quick_replies: list[dict[str, Any]] = Field(None, alias="quick_replies")
    text: str = Field(None, alias="text")
