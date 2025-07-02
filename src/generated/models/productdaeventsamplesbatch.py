"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductDaEventSamplesBatchField = Literal["samples", "time_start", "time_stop"]


class ProductDaEventSamplesBatchFields(BaseModel):
    """Pydantic model for ProductDaEventSamplesBatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    samples: list[dict[str, Any]] = Field(None, alias="samples")
    time_start: int = Field(None, alias="time_start")
    time_stop: int = Field(None, alias="time_stop")
