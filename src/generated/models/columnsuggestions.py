"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ColumnSuggestionsField = Literal["explanations", "format", "objective", "optimization_goals"]


class ColumnSuggestionsFields(BaseModel):
    """Pydantic model for ColumnSuggestions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    explanations: dict[str, Any] = Field(None, alias="explanations")
    format: list[str] = Field(None, alias="format")
    objective: list[str] = Field(None, alias="objective")
    optimization_goals: list[str] = Field(None, alias="optimization_goals")
