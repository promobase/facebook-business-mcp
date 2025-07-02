"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AIGeneratedProductImageField = Literal["flagged_for_manual_review", "transformed_image_url"]


class AIGeneratedProductImageFields(BaseModel):
    """Pydantic model for AIGeneratedProductImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    flagged_for_manual_review: bool = Field(None, alias="flagged_for_manual_review")
    transformed_image_url: str = Field(None, alias="transformed_image_url")
