"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .insightsvalue import InsightsValueFields


# Field literal type
InsightsResultField = Literal[
    "description", "description_from_api_doc", "id", "name", "period", "title", "values"
]


class InsightsResultFields(BaseModel):
    """Pydantic model for InsightsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    description_from_api_doc: str = Field(None, alias="description_from_api_doc")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    period: str = Field(None, alias="period")
    title: str = Field(None, alias="title")
    values: list[InsightsValueFields] = Field(None, alias="values")
