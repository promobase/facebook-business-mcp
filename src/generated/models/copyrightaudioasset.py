"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CopyrightAudioAssetField = Literal[
    "audio_availability_status",
    "audio_library_policy",
    "creation_time",
    "id",
    "reference_files",
    "title",
    "update_time",
]


class CopyrightAudioAssetFields(BaseModel):
    """Pydantic model for CopyrightAudioAsset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_availability_status: str = Field(None, alias="audio_availability_status")
    audio_library_policy: list[dict[str, list[dict[str, dict[str, Any]]]]] = Field(
        None, alias="audio_library_policy"
    )
    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    reference_files: list[dict[str, Any]] = Field(None, alias="reference_files")
    title: str = Field(None, alias="title")
    update_time: datetime = Field(None, alias="update_time")
