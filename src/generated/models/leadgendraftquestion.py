"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenconditionalquestionsgroupchoices import (
        LeadGenConditionalQuestionsGroupChoicesFields,
    )
    from .leadgenconditionalquestionsgroupquestions import (
        LeadGenConditionalQuestionsGroupQuestionsFields,
    )
    from .leadgenquestionoption import LeadGenQuestionOptionFields


# Field literal type
LeadGenDraftQuestionField = Literal[
    "conditional_questions_choices",
    "conditional_questions_group_id",
    "dependent_conditional_questions",
    "inline_context",
    "key",
    "label",
    "options",
    "type",
]


class LeadGenDraftQuestionFields(BaseModel):
    """Pydantic model for LeadGenDraftQuestion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    conditional_questions_choices: list[LeadGenConditionalQuestionsGroupChoicesFields] = Field(
        None, alias="conditional_questions_choices"
    )
    conditional_questions_group_id: str = Field(None, alias="conditional_questions_group_id")
    dependent_conditional_questions: list[LeadGenConditionalQuestionsGroupQuestionsFields] = Field(
        None, alias="dependent_conditional_questions"
    )
    inline_context: str = Field(None, alias="inline_context")
    key: str = Field(None, alias="key")
    label: str = Field(None, alias="label")
    options: list[LeadGenQuestionOptionFields] = Field(None, alias="options")
    type: str = Field(None, alias="type")
