"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WhitehatFBDLRunField = Literal[
    "creation_time", "id", "is_pinned", "note", "result", "run_code", "status", "user_type"
]


class WhitehatFBDLRunFields(BaseModel):
    """Pydantic model for WhitehatFBDLRun fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    is_pinned: bool = Field(None, alias="is_pinned")
    note: str = Field(None, alias="note")
    result: list[dict[str, str]] = Field(None, alias="result")
    run_code: str = Field(None, alias="run_code")
    status: str = Field(None, alias="status")
    user_type: str = Field(None, alias="user_type")
