"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdRuleFilters_operator(str, Enum):
    """AdRuleFilters_operator enum values."""

    ALL = "ALL"
    ANY = "ANY"
    CONTAIN = "CONTAIN"
    EQUAL = "EQUAL"
    GREATER_THAN = "GREATER_THAN"
    IN = "IN"
    IN_RANGE = "IN_RANGE"
    LESS_THAN = "LESS_THAN"
    NONE = "NONE"
    NOT_CONTAIN = "NOT_CONTAIN"
    NOT_EQUAL = "NOT_EQUAL"
    NOT_IN = "NOT_IN"
    NOT_IN_RANGE = "NOT_IN_RANGE"


# Field literal type
AdRuleFiltersField = Literal["field", "operator", "value"]


class AdRuleFiltersFields(BaseModel):
    """Pydantic model for AdRuleFilters fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field: str = Field(None, alias="field")
    operator: dict[str, Any] = Field(None, alias="operator")
    value: dict[str, Any] = Field(None, alias="value")
