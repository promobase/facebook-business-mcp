"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ScimCompanyUserPhoneNumberField = Literal["number", "primary", "type"]


class ScimCompanyUserPhoneNumberFields(BaseModel):
    """Pydantic model for ScimCompanyUserPhoneNumber fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    number: str = Field(None, alias="number")
    primary: bool = Field(None, alias="primary")
    type: str = Field(None, alias="type")
