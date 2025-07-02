"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceStatusField = Literal["code", "description"]


class CustomAudienceStatusFields(BaseModel):
    """Pydantic model for CustomAudienceStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    code: int = Field(None, alias="code")
    description: str = Field(None, alias="description")
