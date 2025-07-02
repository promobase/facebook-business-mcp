"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
CloudGameField = Literal[
    "id",
    "name",
    "owner",
    "playable_ad_file_size",
    "playable_ad_orientation",
    "playable_ad_package_name",
    "playable_ad_reject_reason",
    "playable_ad_status",
    "playable_ad_upload_time",
]


class CloudGameFields(BaseModel):
    """Pydantic model for CloudGame fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner: ProfileFields = Field(None, alias="owner")
    playable_ad_file_size: int = Field(None, alias="playable_ad_file_size")
    playable_ad_orientation: str = Field(None, alias="playable_ad_orientation")
    playable_ad_package_name: str = Field(None, alias="playable_ad_package_name")
    playable_ad_reject_reason: str = Field(None, alias="playable_ad_reject_reason")
    playable_ad_status: str = Field(None, alias="playable_ad_status")
    playable_ad_upload_time: datetime = Field(None, alias="playable_ad_upload_time")
