"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgencontextcard import LeadGenContextCardFields
    from .leadgenlegalcontent import LeadGenLegalContentFields
    from .leadgenquestion import LeadGenQuestionFields
    from .leadgenthankyoupage import LeadGenThankYouPageFields
    from .page import PageFields
    from .user import UserFields


# Field literal type
LeadgenFormField = Literal[
    "allow_organic_lead",
    "block_display_for_non_targeted_viewer",
    "context_card",
    "created_time",
    "creator",
    "expired_leads_count",
    "follow_up_action_text",
    "follow_up_action_url",
    "id",
    "is_optimized_for_quality",
    "leads_count",
    "legal_content",
    "locale",
    "name",
    "organic_leads_count",
    "page",
    "page_id",
    "privacy_policy_url",
    "question_page_custom_headline",
    "questions",
    "status",
    "thank_you_page",
    "tracking_parameters",
]


class LeadgenFormFields(BaseModel):
    """Pydantic model for LeadgenForm fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    allow_organic_lead: bool = Field(None, alias="allow_organic_lead")
    block_display_for_non_targeted_viewer: bool = Field(
        None, alias="block_display_for_non_targeted_viewer"
    )
    context_card: LeadGenContextCardFields = Field(None, alias="context_card")
    created_time: datetime = Field(None, alias="created_time")
    creator: UserFields = Field(None, alias="creator")
    expired_leads_count: int = Field(None, alias="expired_leads_count")
    follow_up_action_text: str = Field(None, alias="follow_up_action_text")
    follow_up_action_url: str = Field(None, alias="follow_up_action_url")
    id: str = Field(None, alias="id")
    is_optimized_for_quality: bool = Field(None, alias="is_optimized_for_quality")
    leads_count: int = Field(None, alias="leads_count")
    legal_content: LeadGenLegalContentFields = Field(None, alias="legal_content")
    locale: str = Field(None, alias="locale")
    name: str = Field(None, alias="name")
    organic_leads_count: int = Field(None, alias="organic_leads_count")
    page: PageFields = Field(None, alias="page")
    page_id: str = Field(None, alias="page_id")
    privacy_policy_url: str = Field(None, alias="privacy_policy_url")
    question_page_custom_headline: str = Field(None, alias="question_page_custom_headline")
    questions: list[LeadGenQuestionFields] = Field(None, alias="questions")
    status: str = Field(None, alias="status")
    thank_you_page: LeadGenThankYouPageFields = Field(None, alias="thank_you_page")
    tracking_parameters: list[dict[str, str]] = Field(None, alias="tracking_parameters")


class LeadgenFormCreateTestLeadParams(BaseModel):
    """Parameters for LeadgenForm.create_test_lead()."""

    model_config = ConfigDict(extra="forbid")
    custom_disclaimer_responses: list[dict[str, Any]] | None = Field(
        None, description="custom_disclaimer_responses parameter"
    )
    field_data: list[dict[str, Any]] | None = Field(None, description="field_data parameter")
