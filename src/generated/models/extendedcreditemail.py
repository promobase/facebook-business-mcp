"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExtendedCreditEmailField = Literal["email", "id"]


class ExtendedCreditEmailFields(BaseModel):
    """Pydantic model for ExtendedCreditEmail fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    email: str = Field(None, alias="email")
    id: str = Field(None, alias="id")
