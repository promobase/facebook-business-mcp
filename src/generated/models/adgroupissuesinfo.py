"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdgroupIssuesInfoField = Literal[
    "error_code", "error_message", "error_summary", "error_type", "level", "mid"
]


class AdgroupIssuesInfoFields(BaseModel):
    """Pydantic model for AdgroupIssuesInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    error_code: int = Field(None, alias="error_code")
    error_message: str = Field(None, alias="error_message")
    error_summary: str = Field(None, alias="error_summary")
    error_type: str = Field(None, alias="error_type")
    level: str = Field(None, alias="level")
    mid: str = Field(None, alias="mid")
