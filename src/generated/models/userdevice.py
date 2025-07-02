"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
UserDeviceField = Literal["hardware", "os"]


class UserDeviceFields(BaseModel):
    """Pydantic model for UserDevice fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    hardware: str = Field(None, alias="hardware")
    os: str = Field(None, alias="os")
