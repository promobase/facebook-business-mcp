"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingAutomationField = Literal[
    "advantage_audience", "individual_setting", "shared_audiences", "value_expression"
]


class TargetingAutomationFields(BaseModel):
    """Pydantic model for TargetingAutomation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    advantage_audience: int = Field(None, alias="advantage_audience")
    individual_setting: dict[str, Any] = Field(None, alias="individual_setting")
    shared_audiences: int = Field(None, alias="shared_audiences")
    value_expression: int = Field(None, alias="value_expression")
