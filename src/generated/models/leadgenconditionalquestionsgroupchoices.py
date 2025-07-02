"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenConditionalQuestionsGroupChoicesField = Literal[
    "customized_token", "next_question_choices", "value"
]


class LeadGenConditionalQuestionsGroupChoicesFields(BaseModel):
    """Pydantic model for LeadGenConditionalQuestionsGroupChoices fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    customized_token: str = Field(None, alias="customized_token")
    next_question_choices: list[LeadGenConditionalQuestionsGroupChoicesFields] = Field(
        None, alias="next_question_choices"
    )
    value: str = Field(None, alias="value")
