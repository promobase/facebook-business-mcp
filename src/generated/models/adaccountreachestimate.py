"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountReachEstimateField = Literal["estimate_ready", "users_lower_bound", "users_upper_bound"]


class AdAccountReachEstimateFields(BaseModel):
    """Pydantic model for AdAccountReachEstimate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    estimate_ready: bool = Field(None, alias="estimate_ready")
    users_lower_bound: int = Field(None, alias="users_lower_bound")
    users_upper_bound: int = Field(None, alias="users_upper_bound")
