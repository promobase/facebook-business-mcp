"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomUserSettingsField = Literal["page_level_persistent_menu", "user_level_persistent_menu"]


class CustomUserSettingsFields(BaseModel):
    """Pydantic model for CustomUserSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    page_level_persistent_menu: list[dict[str, Any]] = Field(
        None, alias="page_level_persistent_menu"
    )
    user_level_persistent_menu: list[dict[str, Any]] = Field(
        None, alias="user_level_persistent_menu"
    )
