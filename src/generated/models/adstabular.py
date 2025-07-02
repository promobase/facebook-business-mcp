"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsTabularField = Literal["rows"]


class AdsTabularFields(BaseModel):
    """Pydantic model for AdsTabular fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    rows: list[dict[str, Any]] = Field(None, alias="rows")
