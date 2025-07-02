"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdStudyObjectiveIDField = Literal["event_names", "id", "type"]


class AdStudyObjectiveIDFields(BaseModel):
    """Pydantic model for AdStudyObjectiveID fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event_names: list[str] = Field(None, alias="event_names")
    id: str = Field(None, alias="id")
    type: str = Field(None, alias="type")
