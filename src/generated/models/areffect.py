"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AREffectField = Literal["creation_time", "id", "last_modified_time", "name", "status", "surfaces"]


class AREffectFields(BaseModel):
    """Pydantic model for AREffect fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    last_modified_time: datetime = Field(None, alias="last_modified_time")
    name: str = Field(None, alias="name")
    status: str = Field(None, alias="status")
    surfaces: list[str] = Field(None, alias="surfaces")
