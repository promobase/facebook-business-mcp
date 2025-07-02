"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LinkedInstagramAccountDataField = Literal[
    "access_token", "analytics_claim", "full_name", "profile_picture_url", "user_id", "user_name"
]


class LinkedInstagramAccountDataFields(BaseModel):
    """Pydantic model for LinkedInstagramAccountData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    access_token: str = Field(None, alias="access_token")
    analytics_claim: str = Field(None, alias="analytics_claim")
    full_name: str = Field(None, alias="full_name")
    profile_picture_url: str = Field(None, alias="profile_picture_url")
    user_id: str = Field(None, alias="user_id")
    user_name: str = Field(None, alias="user_name")
