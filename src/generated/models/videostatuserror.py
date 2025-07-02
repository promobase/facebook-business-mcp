"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoStatusErrorField = Literal["code", "message"]


class VideoStatusErrorFields(BaseModel):
    """Pydantic model for VideoStatusError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    code: int = Field(None, alias="code")
    message: str = Field(None, alias="message")
