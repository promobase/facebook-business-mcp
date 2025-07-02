"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgencustomdisclaimer import LeadGenCustomDisclaimerFields
    from .leadgenprivacypolicy import LeadGenPrivacyPolicyFields


# Field literal type
LeadGenLegalContentField = Literal["custom_disclaimer", "id", "privacy_policy"]


class LeadGenLegalContentFields(BaseModel):
    """Pydantic model for LeadGenLegalContent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_disclaimer: LeadGenCustomDisclaimerFields = Field(None, alias="custom_disclaimer")
    id: str = Field(None, alias="id")
    privacy_policy: LeadGenPrivacyPolicyFields = Field(None, alias="privacy_policy")
