"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessengerProfileField = Literal[
    "account_linking_url",
    "commands",
    "get_started",
    "greeting",
    "ice_breakers",
    "persistent_menu",
    "subject_to_new_eu_privacy_rules",
    "whitelisted_domains",
]


class MessengerProfileFields(BaseModel):
    """Pydantic model for MessengerProfile fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_linking_url: str = Field(None, alias="account_linking_url")
    commands: list[dict[str, Any]] = Field(None, alias="commands")
    get_started: dict[str, Any] = Field(None, alias="get_started")
    greeting: list[dict[str, Any]] = Field(None, alias="greeting")
    ice_breakers: list[dict[str, Any]] = Field(None, alias="ice_breakers")
    persistent_menu: list[dict[str, Any]] = Field(None, alias="persistent_menu")
    subject_to_new_eu_privacy_rules: bool = Field(None, alias="subject_to_new_eu_privacy_rules")
    whitelisted_domains: list[str] = Field(None, alias="whitelisted_domains")
