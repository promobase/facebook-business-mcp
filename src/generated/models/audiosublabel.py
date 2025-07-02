"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudioSubLabelField = Literal[
    "expiration_timestamp",
    "flagged_timestamp",
    "id",
    "label_name",
    "last_update_timestamp",
    "num_audio_tracks",
    "state",
]


class AudioSubLabelFields(BaseModel):
    """Pydantic model for AudioSubLabel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    expiration_timestamp: datetime = Field(None, alias="expiration_timestamp")
    flagged_timestamp: datetime = Field(None, alias="flagged_timestamp")
    id: str = Field(None, alias="id")
    label_name: str = Field(None, alias="label_name")
    last_update_timestamp: datetime = Field(None, alias="last_update_timestamp")
    num_audio_tracks: int = Field(None, alias="num_audio_tracks")
    state: str = Field(None, alias="state")
