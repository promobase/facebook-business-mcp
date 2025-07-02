"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgencustomdisclaimerbody import LeadGenCustomDisclaimerBodyFields
    from .leadgenlegalcontentcheckbox import LeadGenLegalContentCheckboxFields


# Field literal type
LeadGenCustomDisclaimerField = Literal["body", "checkboxes", "title"]


class LeadGenCustomDisclaimerFields(BaseModel):
    """Pydantic model for LeadGenCustomDisclaimer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    body: LeadGenCustomDisclaimerBodyFields = Field(None, alias="body")
    checkboxes: list[LeadGenLegalContentCheckboxFields] = Field(None, alias="checkboxes")
    title: str = Field(None, alias="title")
