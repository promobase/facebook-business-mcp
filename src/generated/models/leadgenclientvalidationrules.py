"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenClientValidationRulesField = Literal[
    "exclude_emoji_and_special_chars_enabled", "max_length_value", "min_length_value"
]


class LeadGenClientValidationRulesFields(BaseModel):
    """Pydantic model for LeadGenClientValidationRules fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    exclude_emoji_and_special_chars_enabled: bool = Field(
        None, alias="exclude_emoji_and_special_chars_enabled"
    )
    max_length_value: int = Field(None, alias="max_length_value")
    min_length_value: int = Field(None, alias="min_length_value")
