"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceSessionField = Literal[
    "end_time",
    "num_invalid_entries",
    "num_matched",
    "num_received",
    "progress",
    "session_id",
    "stage",
    "start_time",
]


class CustomAudienceSessionFields(BaseModel):
    """Pydantic model for CustomAudienceSession fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: str = Field(None, alias="end_time")
    num_invalid_entries: str = Field(None, alias="num_invalid_entries")
    num_matched: str = Field(None, alias="num_matched")
    num_received: str = Field(None, alias="num_received")
    progress: str = Field(None, alias="progress")
    session_id: str = Field(None, alias="session_id")
    stage: str = Field(None, alias="stage")
    start_time: str = Field(None, alias="start_time")
