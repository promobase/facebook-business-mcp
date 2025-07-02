"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AsyncRequestField = Literal["id", "result", "status", "type"]


class AsyncRequestFields(BaseModel):
    """Pydantic model for AsyncRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: int = Field(None, alias="id")
    result: str = Field(None, alias="result")
    status: int = Field(None, alias="status")
    type: int = Field(None, alias="type")
