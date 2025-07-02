"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGShoppingReviewStatusReasonWithHelpMessageField = Literal["code", "help_url", "message"]


class IGShoppingReviewStatusReasonWithHelpMessageFields(BaseModel):
    """Pydantic model for IGShoppingReviewStatusReasonWithHelpMessage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    code: str = Field(None, alias="code")
    help_url: str = Field(None, alias="help_url")
    message: str = Field(None, alias="message")
