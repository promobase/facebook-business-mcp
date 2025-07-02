"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountUserField = Literal["id", "name", "tasks"]


class AdAccountUserFields(BaseModel):
    """Pydantic model for AdAccountUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    tasks: list[str] = Field(None, alias="tasks")
