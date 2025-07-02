"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ContentPublishingLimitResponseField = Literal["config", "quota_usage"]


class ContentPublishingLimitResponseFields(BaseModel):
    """Pydantic model for ContentPublishingLimitResponse fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    config: dict[str, Any] = Field(None, alias="config")
    quota_usage: int = Field(None, alias="quota_usage")
