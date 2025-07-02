"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenPostSubmissionCheckResultField = Literal[
    "api_call_result", "api_error_message", "shown_thank_you_page"
]


class LeadGenPostSubmissionCheckResultFields(BaseModel):
    """Pydantic model for LeadGenPostSubmissionCheckResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    api_call_result: str = Field(None, alias="api_call_result")
    api_error_message: str = Field(None, alias="api_error_message")
    shown_thank_you_page: str = Field(None, alias="shown_thank_you_page")
