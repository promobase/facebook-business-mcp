"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserMobileConfigField = Literal["section_name", "value"]


class UserMobileConfigFields(BaseModel):
    """Pydantic model for UserMobileConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    section_name: str = Field(None, alias="section_name")
    value: dict[str, Any] = Field(None, alias="value")
