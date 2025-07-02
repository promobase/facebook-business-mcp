"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PermissionField = Literal["permission", "status"]


class PermissionFields(BaseModel):
    """Pydantic model for Permission fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    permission: str = Field(None, alias="permission")
    status: str = Field(None, alias="status")
