"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenform import LeadgenFormFields
    from .page import PageFields


# Field literal type
MessengerAdsPartialAutomatedStepListField = Literal[
    "fblead_form",
    "first_step_id",
    "id",
    "page",
    "privacy_url",
    "reminder_text",
    "stop_question_message",
]


class MessengerAdsPartialAutomatedStepListFields(BaseModel):
    """Pydantic model for MessengerAdsPartialAutomatedStepList fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    fblead_form: LeadgenFormFields = Field(None, alias="fblead_form")
    first_step_id: str = Field(None, alias="first_step_id")
    id: str = Field(None, alias="id")
    page: PageFields = Field(None, alias="page")
    privacy_url: str = Field(None, alias="privacy_url")
    reminder_text: str = Field(None, alias="reminder_text")
    stop_question_message: str = Field(None, alias="stop_question_message")
