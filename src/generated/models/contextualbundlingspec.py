"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ContextualBundlingSpecField = Literal["status"]


class ContextualBundlingSpecFields(BaseModel):
    """Pydantic model for ContextualBundlingSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    status: str = Field(None, alias="status")
