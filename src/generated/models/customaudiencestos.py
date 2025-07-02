"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudiencesTOSField = Literal["content", "id", "type"]


class CustomAudiencesTOSFields(BaseModel):
    """Pydantic model for CustomAudiencesTOS fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content: str = Field(None, alias="content")
    id: str = Field(None, alias="id")
    type: str = Field(None, alias="type")
