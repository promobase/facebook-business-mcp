"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targeting import TargetingFields


# Field literal type
TargetingSentenceLineField = Literal["id", "params", "targetingsentencelines"]


class TargetingSentenceLineFields(BaseModel):
    """Pydantic model for TargetingSentenceLine fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    params: TargetingFields = Field(None, alias="params")
    targetingsentencelines: dict[str, Any] = Field(None, alias="targetingsentencelines")
