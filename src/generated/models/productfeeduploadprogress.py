"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedUploadProgressField = Literal["pos", "size", "step", "unit", "updated_time"]


class ProductFeedUploadProgressFields(BaseModel):
    """Pydantic model for ProductFeedUploadProgress fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    pos: int = Field(None, alias="pos")
    size: int = Field(None, alias="size")
    step: str = Field(None, alias="step")
    unit: str = Field(None, alias="unit")
    updated_time: datetime = Field(None, alias="updated_time")
