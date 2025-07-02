"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingRelaxationField = Literal["custom_audience", "lookalike"]


class TargetingRelaxationFields(BaseModel):
    """Pydantic model for TargetingRelaxation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_audience: int = Field(None, alias="custom_audience")
    lookalike: int = Field(None, alias="lookalike")
