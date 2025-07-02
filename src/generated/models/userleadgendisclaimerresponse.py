"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserLeadGenDisclaimerResponseField = Literal["checkbox_key", "is_checked"]


class UserLeadGenDisclaimerResponseFields(BaseModel):
    """Pydantic model for UserLeadGenDisclaimerResponse fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    checkbox_key: str = Field(None, alias="checkbox_key")
    is_checked: str = Field(None, alias="is_checked")
