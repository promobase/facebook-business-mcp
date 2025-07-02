"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adruleexecutionoptions import AdRuleExecutionOptionsFields


class AdRuleExecutionSpec_execution_type(str, Enum):
    """AdRuleExecutionSpec_execution_type enum values."""

    ADD_INTEREST_RELAXATION = "ADD_INTEREST_RELAXATION"
    ADD_QUESTIONNAIRE_INTERESTS = "ADD_QUESTIONNAIRE_INTERESTS"
    AD_RECOMMENDATION_APPLY = "AD_RECOMMENDATION_APPLY"
    AUDIENCE_CONSOLIDATION = "AUDIENCE_CONSOLIDATION"
    AUDIENCE_CONSOLIDATION_ASK_FIRST = "AUDIENCE_CONSOLIDATION_ASK_FIRST"
    CHANGE_BID = "CHANGE_BID"
    CHANGE_BUDGET = "CHANGE_BUDGET"
    CHANGE_CAMPAIGN_BUDGET = "CHANGE_CAMPAIGN_BUDGET"
    DCO = "DCO"
    INCREASE_RADIUS = "INCREASE_RADIUS"
    NOTIFICATION = "NOTIFICATION"
    PAUSE = "PAUSE"
    PING_ENDPOINT = "PING_ENDPOINT"
    REBALANCE_BUDGET = "REBALANCE_BUDGET"
    ROTATE = "ROTATE"
    UNPAUSE = "UNPAUSE"
    UPDATE_CREATIVE = "UPDATE_CREATIVE"
    UPDATE_LAX_BUDGET = "UPDATE_LAX_BUDGET"
    UPDATE_LAX_DURATION = "UPDATE_LAX_DURATION"


# Field literal type
AdRuleExecutionSpecField = Literal["execution_options", "execution_type", "is_once_off"]


class AdRuleExecutionSpecFields(BaseModel):
    """Pydantic model for AdRuleExecutionSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    execution_options: list[AdRuleExecutionOptionsFields] = Field(None, alias="execution_options")
    execution_type: dict[str, Any] = Field(None, alias="execution_type")
    is_once_off: bool = Field(None, alias="is_once_off")
