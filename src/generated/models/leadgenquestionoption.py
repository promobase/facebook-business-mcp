"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenQuestionOptionField = Literal["key", "value"]


class LeadGenQuestionOptionFields(BaseModel):
    """Pydantic model for LeadGenQuestionOption fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    key: str = Field(None, alias="key")
    value: str = Field(None, alias="value")
