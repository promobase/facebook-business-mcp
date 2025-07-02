"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreative import AdCreativeFields


# Field literal type
UniqueAdCreativeField = Literal["sample_creative", "visual_hash"]


class UniqueAdCreativeFields(BaseModel):
    """Pydantic model for UniqueAdCreative fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    sample_creative: AdCreativeFields = Field(None, alias="sample_creative")
    visual_hash: int = Field(None, alias="visual_hash")
