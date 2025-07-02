"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .instagraminsightsvalue import InstagramInsightsValueFields


# Field literal type
InstagramInsightsResultField = Literal[
    "description", "id", "name", "period", "title", "total_value", "values"
]


class InstagramInsightsResultFields(BaseModel):
    """Pydantic model for InstagramInsightsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    period: str = Field(None, alias="period")
    title: str = Field(None, alias="title")
    total_value: dict[str, Any] = Field(None, alias="total_value")
    values: list[InstagramInsightsValueFields] = Field(None, alias="values")
