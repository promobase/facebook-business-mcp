"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenPrivacyPolicyField = Literal["link_text", "url"]


class LeadGenPrivacyPolicyFields(BaseModel):
    """Pydantic model for LeadGenPrivacyPolicy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    link_text: str = Field(None, alias="link_text")
    url: str = Field(None, alias="url")
