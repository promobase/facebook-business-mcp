"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ChatPluginField = Literal[
    "alignment",
    "desktop_bottom_spacing",
    "desktop_side_spacing",
    "entry_point_icon",
    "entry_point_label",
    "greeting_dialog_display",
    "guest_chat_mode",
    "mobile_bottom_spacing",
    "mobile_chat_display",
    "mobile_side_spacing",
    "theme_color",
    "welcome_screen_greeting",
]


class ChatPluginFields(BaseModel):
    """Pydantic model for ChatPlugin fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    alignment: str = Field(None, alias="alignment")
    desktop_bottom_spacing: str = Field(None, alias="desktop_bottom_spacing")
    desktop_side_spacing: str = Field(None, alias="desktop_side_spacing")
    entry_point_icon: str = Field(None, alias="entry_point_icon")
    entry_point_label: str = Field(None, alias="entry_point_label")
    greeting_dialog_display: str = Field(None, alias="greeting_dialog_display")
    guest_chat_mode: str = Field(None, alias="guest_chat_mode")
    mobile_bottom_spacing: str = Field(None, alias="mobile_bottom_spacing")
    mobile_chat_display: str = Field(None, alias="mobile_chat_display")
    mobile_side_spacing: str = Field(None, alias="mobile_side_spacing")
    theme_color: str = Field(None, alias="theme_color")
    welcome_screen_greeting: str = Field(None, alias="welcome_screen_greeting")
