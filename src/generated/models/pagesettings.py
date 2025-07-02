"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageSettingsField = Literal["setting", "value"]


class PageSettingsFields(BaseModel):
    """Pydantic model for PageSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    setting: str = Field(None, alias="setting")
    value: dict[str, Any] = Field(None, alias="value")
