"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenLegalContentCheckboxField = Literal[
    "id", "is_checked_by_default", "is_required", "key", "text"
]


class LeadGenLegalContentCheckboxFields(BaseModel):
    """Pydantic model for LeadGenLegalContentCheckbox fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    is_checked_by_default: bool = Field(None, alias="is_checked_by_default")
    is_required: bool = Field(None, alias="is_required")
    key: str = Field(None, alias="key")
    text: str = Field(None, alias="text")
