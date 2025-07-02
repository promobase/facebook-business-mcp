"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LiveVideoErrorField = Literal["creation_time", "error_code", "error_message", "error_type"]


class LiveVideoErrorFields(BaseModel):
    """Pydantic model for LiveVideoError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    error_code: int = Field(None, alias="error_code")
    error_message: str = Field(None, alias="error_message")
    error_type: str = Field(None, alias="error_type")
