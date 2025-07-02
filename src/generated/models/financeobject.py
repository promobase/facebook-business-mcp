"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
FinanceObjectField = Literal["finance_permission", "user"]


class FinanceObjectFields(BaseModel):
    """Pydantic model for FinanceObject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    finance_permission: str = Field(None, alias="finance_permission")
    user: dict[str, Any] = Field(None, alias="user")
