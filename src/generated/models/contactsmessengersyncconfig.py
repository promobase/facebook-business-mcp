"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ContactsMessengerSyncConfigField = Literal["enabled"]


class ContactsMessengerSyncConfigFields(BaseModel):
    """Pydantic model for ContactsMessengerSyncConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    enabled: bool = Field(None, alias="enabled")
