"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdStudyObjectiveField = Literal[
    "id", "is_primary", "last_updated_results", "name", "results", "type"
]


class AdStudyObjectiveFields(BaseModel):
    """Pydantic model for AdStudyObjective fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    is_primary: bool = Field(None, alias="is_primary")
    last_updated_results: str = Field(None, alias="last_updated_results")
    name: str = Field(None, alias="name")
    results: list[str] = Field(None, alias="results")
    type: str = Field(None, alias="type")
