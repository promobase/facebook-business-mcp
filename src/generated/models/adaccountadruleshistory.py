"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adruleevaluationspec import AdRuleEvaluationSpecFields
    from .adruleexecutionspec import AdRuleExecutionSpecFields
    from .adrulehistoryresult import AdRuleHistoryResultFields
    from .adruleschedulespec import AdRuleScheduleSpecFields


# Field literal type
AdAccountAdRulesHistoryField = Literal[
    "evaluation_spec",
    "exception_code",
    "exception_message",
    "execution_spec",
    "is_manual",
    "results",
    "rule_id",
    "schedule_spec",
    "timestamp",
]


class AdAccountAdRulesHistoryFields(BaseModel):
    """Pydantic model for AdAccountAdRulesHistory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    evaluation_spec: AdRuleEvaluationSpecFields = Field(None, alias="evaluation_spec")
    exception_code: int = Field(None, alias="exception_code")
    exception_message: str = Field(None, alias="exception_message")
    execution_spec: AdRuleExecutionSpecFields = Field(None, alias="execution_spec")
    is_manual: bool = Field(None, alias="is_manual")
    results: list[AdRuleHistoryResultFields] = Field(None, alias="results")
    rule_id: int = Field(None, alias="rule_id")
    schedule_spec: AdRuleScheduleSpecFields = Field(None, alias="schedule_spec")
    timestamp: datetime = Field(None, alias="timestamp")
