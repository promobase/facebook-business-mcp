"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PrivacyField = Literal["allow", "deny", "description", "friends", "networks", "value"]


class PrivacyFields(BaseModel):
    """Pydantic model for Privacy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    allow: str = Field(None, alias="allow")
    deny: str = Field(None, alias="deny")
    description: str = Field(None, alias="description")
    friends: str = Field(None, alias="friends")
    networks: str = Field(None, alias="networks")
    value: str = Field(None, alias="value")
