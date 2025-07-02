"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdRuleTrigger_operator(str, Enum):
    """AdRuleTrigger_operator enum values."""

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


class AdRuleTrigger_type(str, Enum):
    """AdRuleTrigger_type enum values."""

    DELIVERY_INSIGHTS_CHANGE = "DELIVERY_INSIGHTS_CHANGE"
    METADATA_CREATION = "METADATA_CREATION"
    METADATA_UPDATE = "METADATA_UPDATE"
    STATS_CHANGE = "STATS_CHANGE"
    STATS_MILESTONE = "STATS_MILESTONE"


# Field literal type
AdRuleTriggerField = Literal["field", "operator", "type", "value"]


class AdRuleTriggerFields(BaseModel):
    """Pydantic model for AdRuleTrigger fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field: str = Field(None, alias="field")
    operator: dict[str, Any] = Field(None, alias="operator")
    type: dict[str, Any] = Field(None, alias="type")
    value: dict[str, Any] = Field(None, alias="value")
