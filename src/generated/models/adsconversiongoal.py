"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsConversionGoalField = Literal[
    "ad_account_id",
    "conversion_event_value_source",
    "description",
    "goal_creation_method",
    "id",
    "name",
    "performance_goal",
    "update_status",
]


class AdsConversionGoalFields(BaseModel):
    """Pydantic model for AdsConversionGoal fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    conversion_event_value_source: str = Field(None, alias="conversion_event_value_source")
    description: str = Field(None, alias="description")
    goal_creation_method: str = Field(None, alias="goal_creation_method")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    performance_goal: str = Field(None, alias="performance_goal")
    update_status: str = Field(None, alias="update_status")
