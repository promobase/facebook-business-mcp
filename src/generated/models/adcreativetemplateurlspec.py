"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeTemplateURLSpecField = Literal[
    "android", "config", "ios", "ipad", "iphone", "web", "windows_phone"
]


class AdCreativeTemplateURLSpecFields(BaseModel):
    """Pydantic model for AdCreativeTemplateURLSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android: dict[str, Any] = Field(None, alias="android")
    config: dict[str, Any] = Field(None, alias="config")
    ios: dict[str, Any] = Field(None, alias="ios")
    ipad: dict[str, Any] = Field(None, alias="ipad")
    iphone: dict[str, Any] = Field(None, alias="iphone")
    web: dict[str, Any] = Field(None, alias="web")
    windows_phone: dict[str, Any] = Field(None, alias="windows_phone")
