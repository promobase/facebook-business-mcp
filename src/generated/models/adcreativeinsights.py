"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeInsightsField = Literal["aesthetics"]


class AdCreativeInsightsFields(BaseModel):
    """Pydantic model for AdCreativeInsights fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    aesthetics: list[dict[str, str]] = Field(None, alias="aesthetics")
