"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgendraftquestion import LeadGenDraftQuestionFields
    from .page import PageFields


# Field literal type
LeadGenDataDraftField = Literal[
    "block_display_for_non_targeted_viewer",
    "created_time",
    "disqualified_end_component",
    "follow_up_action_url",
    "id",
    "is_optimized_for_quality",
    "legal_content",
    "locale",
    "name",
    "page",
    "question_page_custom_headline",
    "questions",
    "status",
    "thank_you_page",
    "tracking_parameters",
]


class LeadGenDataDraftFields(BaseModel):
    """Pydantic model for LeadGenDataDraft fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    block_display_for_non_targeted_viewer: bool = Field(
        None, alias="block_display_for_non_targeted_viewer"
    )
    created_time: datetime = Field(None, alias="created_time")
    disqualified_end_component: dict[str, Any] = Field(None, alias="disqualified_end_component")
    follow_up_action_url: str = Field(None, alias="follow_up_action_url")
    id: str = Field(None, alias="id")
    is_optimized_for_quality: bool = Field(None, alias="is_optimized_for_quality")
    legal_content: dict[str, Any] = Field(None, alias="legal_content")
    locale: str = Field(None, alias="locale")
    name: str = Field(None, alias="name")
    page: PageFields = Field(None, alias="page")
    question_page_custom_headline: str = Field(None, alias="question_page_custom_headline")
    questions: list[LeadGenDraftQuestionFields] = Field(None, alias="questions")
    status: str = Field(None, alias="status")
    thank_you_page: dict[str, Any] = Field(None, alias="thank_you_page")
    tracking_parameters: list[dict[str, str]] = Field(None, alias="tracking_parameters")
