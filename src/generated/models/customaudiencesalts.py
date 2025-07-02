"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceSaltsField = Literal["app_id", "public_key", "salts", "user_id"]


class CustomAudienceSaltsFields(BaseModel):
    """Pydantic model for CustomAudienceSalts fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: int = Field(None, alias="app_id")
    public_key: str = Field(None, alias="public_key")
    salts: list[dict[str, Any]] = Field(None, alias="salts")
    user_id: int = Field(None, alias="user_id")
