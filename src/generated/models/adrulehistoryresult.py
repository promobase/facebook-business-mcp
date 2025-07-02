"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adrulehistoryresultaction import AdRuleHistoryResultActionFields


class AdRuleHistoryResult_object_type(str, Enum):
    """AdRuleHistoryResult_object_type enum values."""

    AD = "AD"
    ADSET = "ADSET"
    CAMPAIGN = "CAMPAIGN"


# Field literal type
AdRuleHistoryResultField = Literal["actions", "object_id", "object_type"]


class AdRuleHistoryResultFields(BaseModel):
    """Pydantic model for AdRuleHistoryResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: list[AdRuleHistoryResultActionFields] = Field(None, alias="actions")
    object_id: str = Field(None, alias="object_id")
    object_type: dict[str, Any] = Field(None, alias="object_type")
