"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WorkUserFrontlineField = Literal["has_access", "is_frontline"]


class WorkUserFrontlineFields(BaseModel):
    """Pydantic model for WorkUserFrontline fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    has_access: bool = Field(None, alias="has_access")
    is_frontline: bool = Field(None, alias="is_frontline")
