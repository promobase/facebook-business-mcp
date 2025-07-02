"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ValueBasedEligibleSourceField = Literal["id", "title", "type"]


class ValueBasedEligibleSourceFields(BaseModel):
    """Pydantic model for ValueBasedEligibleSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    title: str = Field(None, alias="title")
    type: str = Field(None, alias="type")
