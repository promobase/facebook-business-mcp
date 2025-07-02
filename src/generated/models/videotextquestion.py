"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoTextQuestionField = Literal["id", "question_target_id", "question_text", "status"]


class VideoTextQuestionFields(BaseModel):
    """Pydantic model for VideoTextQuestion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    question_target_id: str = Field(None, alias="question_target_id")
    question_text: str = Field(None, alias="question_text")
    status: str = Field(None, alias="status")
