"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdRuleExecutionOptions_operator(str, Enum):
    """AdRuleExecutionOptions_operator enum values."""

    EQUAL = "EQUAL"
    IN = "IN"


# Field literal type
AdRuleExecutionOptionsField = Literal["field", "operator", "value"]


class AdRuleExecutionOptionsFields(BaseModel):
    """Pydantic model for AdRuleExecutionOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field: str = Field(None, alias="field")
    operator: dict[str, Any] = Field(None, alias="operator")
    value: dict[str, Any] = Field(None, alias="value")
