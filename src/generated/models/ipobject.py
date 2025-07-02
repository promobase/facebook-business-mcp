"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IPObjectField = Literal["ip_permission", "user"]


class IPObjectFields(BaseModel):
    """Pydantic model for IPObject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ip_permission: str = Field(None, alias="ip_permission")
    user: dict[str, Any] = Field(None, alias="user")
