"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenConditionalQuestionsGroupQuestionsField = Literal["field_key", "input_type", "name"]


class LeadGenConditionalQuestionsGroupQuestionsFields(BaseModel):
    """Pydantic model for LeadGenConditionalQuestionsGroupQuestions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field_key: str = Field(None, alias="field_key")
    input_type: str = Field(None, alias="input_type")
    name: str = Field(None, alias="name")
