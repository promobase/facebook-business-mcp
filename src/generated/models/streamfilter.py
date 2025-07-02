"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
StreamFilterField = Literal["filter_key", "name", "type"]


class StreamFilterFields(BaseModel):
    """Pydantic model for StreamFilter fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    filter_key: str = Field(None, alias="filter_key")
    name: str = Field(None, alias="name")
    type: str = Field(None, alias="type")
