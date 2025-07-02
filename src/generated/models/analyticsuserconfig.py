"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsUserConfigField = Literal["demo_app_nux_config", "flags", "id"]


class AnalyticsUserConfigFields(BaseModel):
    """Pydantic model for AnalyticsUserConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    demo_app_nux_config: dict[str, Any] = Field(None, alias="demo_app_nux_config")
    flags: list[dict[str, str]] = Field(None, alias="flags")
    id: str = Field(None, alias="id")
