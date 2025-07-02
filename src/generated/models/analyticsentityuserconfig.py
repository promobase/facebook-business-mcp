"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsEntityUserConfigField = Literal["dismissed_notices"]


class AnalyticsEntityUserConfigFields(BaseModel):
    """Pydantic model for AnalyticsEntityUserConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    dismissed_notices: list[str] = Field(None, alias="dismissed_notices")
