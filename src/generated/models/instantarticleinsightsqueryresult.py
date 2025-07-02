"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstantArticleInsightsQueryResultField = Literal["breakdowns", "name", "time", "value"]


class InstantArticleInsightsQueryResultFields(BaseModel):
    """Pydantic model for InstantArticleInsightsQueryResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    breakdowns: dict[str, str] = Field(None, alias="breakdowns")
    name: str = Field(None, alias="name")
    time: datetime = Field(None, alias="time")
    value: str = Field(None, alias="value")
