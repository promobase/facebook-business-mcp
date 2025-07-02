"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DACheckField = Literal["action_uri", "description", "key", "result", "title", "user_message"]


class DACheckFields(BaseModel):
    """Pydantic model for DACheck fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_uri: str = Field(None, alias="action_uri")
    description: str = Field(None, alias="description")
    key: str = Field(None, alias="key")
    result: str = Field(None, alias="result")
    title: str = Field(None, alias="title")
    user_message: str = Field(None, alias="user_message")
