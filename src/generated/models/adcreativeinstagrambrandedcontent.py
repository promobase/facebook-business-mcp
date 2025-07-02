"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeInstagramBrandedContentField = Literal["sponsor_id"]


class AdCreativeInstagramBrandedContentFields(BaseModel):
    """Pydantic model for AdCreativeInstagramBrandedContent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    sponsor_id: str = Field(None, alias="sponsor_id")
