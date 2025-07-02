"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adrulefilters import AdRuleFiltersFields
    from .adruletrigger import AdRuleTriggerFields


class AdRuleEvaluationSpec_evaluation_type(str, Enum):
    """AdRuleEvaluationSpec_evaluation_type enum values."""

    SCHEDULE = "SCHEDULE"
    TRIGGER = "TRIGGER"


# Field literal type
AdRuleEvaluationSpecField = Literal["evaluation_type", "filters", "trigger"]


class AdRuleEvaluationSpecFields(BaseModel):
    """Pydantic model for AdRuleEvaluationSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    evaluation_type: dict[str, Any] = Field(None, alias="evaluation_type")
    filters: list[AdRuleFiltersFields] = Field(None, alias="filters")
    trigger: AdRuleTriggerFields = Field(None, alias="trigger")
