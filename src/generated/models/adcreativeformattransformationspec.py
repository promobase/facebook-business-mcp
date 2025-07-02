"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeFormatTransformationSpecField = Literal["data_source", "format"]


class AdCreativeFormatTransformationSpecFields(BaseModel):
    """Pydantic model for AdCreativeFormatTransformationSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    data_source: list[str] = Field(None, alias="data_source")
    format: str = Field(None, alias="format")
