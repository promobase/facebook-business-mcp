"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountAdRulesCountByTypeField = Literal["count", "evaluation_type"]


class AdAccountAdRulesCountByTypeFields(BaseModel):
    """Pydantic model for AdAccountAdRulesCountByType fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    count: int = Field(None, alias="count")
    evaluation_type: str = Field(None, alias="evaluation_type")
