"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BlockedUserInfoField = Literal["block_time", "block_type", "fbid", "name", "username"]


class BlockedUserInfoFields(BaseModel):
    """Pydantic model for BlockedUserInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    block_time: datetime = Field(None, alias="block_time")
    block_type: str = Field(None, alias="block_type")
    fbid: str = Field(None, alias="fbid")
    name: str = Field(None, alias="name")
    username: str = Field(None, alias="username")
