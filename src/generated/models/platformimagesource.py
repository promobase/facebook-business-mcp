"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PlatformImageSourceField = Literal["height", "source", "width"]


class PlatformImageSourceFields(BaseModel):
    """Pydantic model for PlatformImageSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    height: int = Field(None, alias="height")
    source: str = Field(None, alias="source")
    width: int = Field(None, alias="width")
