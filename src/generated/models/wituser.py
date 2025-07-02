"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WITUserField = Literal["access_token", "id", "name"]


class WITUserFields(BaseModel):
    """Pydantic model for WITUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    access_token: str = Field(None, alias="access_token")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
