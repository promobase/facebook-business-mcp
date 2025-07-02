"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudienceOverlapField = Literal["estimated_reach", "id", "name", "overlap"]


class AudienceOverlapFields(BaseModel):
    """Pydantic model for AudienceOverlap fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    estimated_reach: int = Field(None, alias="estimated_reach")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    overlap: int = Field(None, alias="overlap")
