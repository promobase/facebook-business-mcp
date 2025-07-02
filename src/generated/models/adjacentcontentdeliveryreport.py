"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdjacentContentDeliveryReportField = Literal["ad_id", "content", "impression_id"]


class AdjacentContentDeliveryReportFields(BaseModel):
    """Pydantic model for AdjacentContentDeliveryReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_id: str = Field(None, alias="ad_id")
    content: list[dict[str, Any]] = Field(None, alias="content")
    impression_id: str = Field(None, alias="impression_id")
