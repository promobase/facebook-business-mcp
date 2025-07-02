"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessagingAppsInfoField = Literal[
    "ctd_support_only_for_ig_app",
    "has_instagram_messaging_permission",
    "has_messenger_messaging_permission",
    "id",
    "name",
]


class MessagingAppsInfoFields(BaseModel):
    """Pydantic model for MessagingAppsInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ctd_support_only_for_ig_app: bool = Field(None, alias="ctd_support_only_for_ig_app")
    has_instagram_messaging_permission: bool = Field(
        None, alias="has_instagram_messaging_permission"
    )
    has_messenger_messaging_permission: bool = Field(
        None, alias="has_messenger_messaging_permission"
    )
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
