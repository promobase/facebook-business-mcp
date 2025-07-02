"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adruleevaluationspec import AdRuleEvaluationSpecFields
    from .adruleexecutionspec import AdRuleExecutionSpecFields
    from .adruleschedulespec import AdRuleScheduleSpecFields
    from .user import UserFields


class adrulehistory_action_enum_param(str, Enum):
    """adrulehistory_action_enum_param enum values."""

    BUDGET_NOT_REDISTRIBUTED = "BUDGET_NOT_REDISTRIBUTED"
    CHANGED_BID = "CHANGED_BID"
    CHANGED_BUDGET = "CHANGED_BUDGET"
    CONSOLIDATE_ASC_FRAGMENTATION = "CONSOLIDATE_ASC_FRAGMENTATION"
    CONSOLIDATE_FRAGMENTATION = "CONSOLIDATE_FRAGMENTATION"
    CONVERT_ASC_CP_SINGLE_INSTANCE = "CONVERT_ASC_CP_SINGLE_INSTANCE"
    EMAIL = "EMAIL"
    ENABLE_ADVANTAGE_CAMPAIGN_BUDGET = "ENABLE_ADVANTAGE_CAMPAIGN_BUDGET"
    ENABLE_ADVANTAGE_PLUS_AUDIENCE = "ENABLE_ADVANTAGE_PLUS_AUDIENCE"
    ENABLE_ADVANTAGE_PLUS_CREATIVE = "ENABLE_ADVANTAGE_PLUS_CREATIVE"
    ENABLE_ADVANTAGE_PLUS_PLACEMENTS = "ENABLE_ADVANTAGE_PLUS_PLACEMENTS"
    ENABLE_AUTOFLOW = "ENABLE_AUTOFLOW"
    ENABLE_GEN_UNCROP = "ENABLE_GEN_UNCROP"
    ENABLE_LANDING_PAGE_VIEWS = "ENABLE_LANDING_PAGE_VIEWS"
    ENABLE_MUSIC = "ENABLE_MUSIC"
    ENABLE_REELS_PLACEMENTS = "ENABLE_REELS_PLACEMENTS"
    ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION = "ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION"
    ENABLE_SHOPS_ADS = "ENABLE_SHOPS_ADS"
    ENDPOINT_PINGED = "ENDPOINT_PINGED"
    ERROR = "ERROR"
    FACEBOOK_NOTIFICATION_SENT = "FACEBOOK_NOTIFICATION_SENT"
    MESSAGE_SENT = "MESSAGE_SENT"
    NOT_CHANGED = "NOT_CHANGED"
    PAUSED = "PAUSED"
    UNPAUSED = "UNPAUSED"


# Field literal type
AdRuleField = Literal[
    "account_id",
    "created_by",
    "created_time",
    "disable_error_code",
    "evaluation_spec",
    "execution_spec",
    "id",
    "name",
    "schedule_spec",
    "status",
    "updated_time",
]


class AdRuleFields(BaseModel):
    """Pydantic model for AdRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    created_by: UserFields = Field(None, alias="created_by")
    created_time: datetime = Field(None, alias="created_time")
    disable_error_code: int = Field(None, alias="disable_error_code")
    evaluation_spec: AdRuleEvaluationSpecFields = Field(None, alias="evaluation_spec")
    execution_spec: AdRuleExecutionSpecFields = Field(None, alias="execution_spec")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    schedule_spec: AdRuleScheduleSpecFields = Field(None, alias="schedule_spec")
    status: str = Field(None, alias="status")
    updated_time: datetime = Field(None, alias="updated_time")


class AdRuleGetHistoryParams(BaseModel):
    """Parameters for AdRule.get_history()."""

    model_config = ConfigDict(extra="forbid")
    action: adrulehistory_action_enum_param | None = Field(None, description="action parameter")
    hide_no_changes: bool | None = Field(None, description="hide_no_changes parameter")
    object_id: str | None = Field(None, description="object_id parameter")
