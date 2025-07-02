"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativePromotionMetadataSpecField = Literal[
    "end_date",
    "id",
    "promotion_source",
    "promotion_type",
    "promotion_value",
    "required_code",
    "start_date",
]


class AdCreativePromotionMetadataSpecFields(BaseModel):
    """Pydantic model for AdCreativePromotionMetadataSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_date: int = Field(None, alias="end_date")
    id: str = Field(None, alias="id")
    promotion_source: str = Field(None, alias="promotion_source")
    promotion_type: str = Field(None, alias="promotion_type")
    promotion_value: float = Field(None, alias="promotion_value")
    required_code: str = Field(None, alias="required_code")
    start_date: int = Field(None, alias="start_date")
