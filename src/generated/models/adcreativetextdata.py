"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeTextDataField = Literal["message"]


class AdCreativeTextDataFields(BaseModel):
    """Pydantic model for AdCreativeTextData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    message: str = Field(None, alias="message")
