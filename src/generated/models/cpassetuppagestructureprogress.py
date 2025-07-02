"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASSetupPageStructureProgressField = Literal["id", "issues", "name"]


class CPASSetupPageStructureProgressFields(BaseModel):
    """Pydantic model for CPASSetupPageStructureProgress fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    issues: list[dict[str, Any]] = Field(None, alias="issues")
    name: str = Field(None, alias="name")
